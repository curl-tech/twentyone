import os
from fastapi import FastAPI, Form
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import File
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
import yaml
from yaml.loader import SafeLoader
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.routers.user import user_router
from Backend.app.routers.project import project_router
from Backend.app.routers.data import data_router
from Backend.app.routers.model import model_router
from Backend.app.routers.metrics import metrics_router
from Backend.app.routers.inference import inference_router
from Backend.app.helpers.allhelpers import reqsEntity, reqEntity, CurrentIDs
from Backend.app.helpers.project_helper import create_project_id, get_project_id, get_raw_data_path
from Backend.app.helpers.model_helper import create_model_id
from Backend.app.schemas import FormData
from Backend.utils import generate_project_folder, generate_random_id
from Files.auto import auto

origins=settings.CORS_ORIGIN

app=FastAPI()

app.include_router(user_router, tags=["user"])
app.include_router(project_router, tags=["project"])
app.include_router(data_router, tags=["data"])
app.include_router(model_router,tags=["model"])
app.include_router(metrics_router,tags=["metrics"])
app.include_router(inference_router,tags=["inference"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Project21Database=Database()
currentIDs=CurrentIDs()
currentIDs.set_current_user_id(101)


@app.get('/')
def home(): 
    return JSONResponse({"Hello": "World","serverStatus":"Working"})

@app.on_event("startup")
def startup_mongodb_client():
    Project21Database.initialise(settings.DB_NAME)
    try:
        Project21Database.insert_one(settings.DB_COLLECTION_USER,{
                "userID":101,
                "name": "John Doe",
                "email": "johndoe@email.com",
                "username": "TheJohnDoe",
                "password": "password@Super@Secure",
                "listOfProjects": []
            })
    except:
        pass

@app.on_event("shutdown")
def shutdown_mongodb_client():
    Project21Database.close()

@app.post('/create')
def create_project(projectName:str=Form(...),mtype:str=Form(...),train: UploadFile=File(...)):
    operation=generate_project_folder(projectName,train)
    if operation["Success"]:
        try:
            inserted_projectID=create_project_id()
            inserted_modelID=create_model_id()
            currentIDs.set_current_project_id(inserted_projectID)
            currentIDs.set_current_model_id(inserted_modelID)
            Project21Database.insert_one(settings.DB_COLLECTION_PROJECT,{
                "projectID":inserted_projectID,
                "projectName":projectName,
                "rawDataPath":operation["RawDataPath"],
                "projectFolderPath":operation["ProjectFolderPath"],
                "belongsToUserID": currentIDs.get_current_user_id()
                })
            Project21Database.insert_one(settings.DB_COLLECTION_MODEL,{
                "modelID": inserted_modelID,
                "modelName": "Default Model",
                "modelType": mtype,
                "belongsToUserID": currentIDs.get_current_user_id(),
                "belongsToProjectID": inserted_projectID
            })
            try:
                result=Project21Database.find_one(settings.DB_COLLECTION_USER,{"userID":currentIDs.get_current_user_id()})
                Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":result["userID"]},{ "listOfProjects":result["listOfProjects"].append(inserted_projectID)})
            except:
                print({"File Received": "Success", "Project Folder":"Success", "Database Update":"Partially Successful"})
        except:
            print({"File Received": "Success","Project Folder":"Success","Database Update":"Failure"})
            return {"File Received": "Success","Project Folder":"Success","Database Update":"Failure"}
        return {"File Received": "Success", "Project Folder":"Success", "Database Update":"Success"}
    else:
        print(operation["Error"])
        return operation["Error"]

# @app.get('/file')
# def file():           #For Streaming files
#     path=get_raw_data_path(45586)       #Have to put projectID here
#     myfile=open(path,mode='rb')
#     return StreamingResponse(myfile,media_type="text/csv")

@app.get('/downloadClean')
def download_clean_data():
    print("current user id: ",currentIDs.get_current_user_id())
    path=get_raw_data_path(68677)       #Have to put dataID here
    if(os.path.exists(path)):
        return FileResponse(path,media_type="text/csv")     #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"File not found at path"}

@app.get('/downloadPickle')
def file_download():
    path=get_raw_data_path(68677)       #Have to put modelID here
    if(os.path.exists(path)):
        return FileResponse(path,media_type="text/csv")     #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"File not found at path"}

@app.post('/auto')
def start_auto_preprocessing(formData:FormData):
    formData=dict(formData)
    user_yaml=yaml.load(open(settings.CONFIG_AUTO_YAML_FILE),Loader=SafeLoader)
    user_yaml["id"]=generate_random_id()
    user_yaml["raw_data_address"]=get_raw_data_path(currentIDs.get_current_project_id())
    user_yaml["target_col_name"]=formData["target"]
    result_model=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":currentIDs.get_current_model_id()})
    # if result_model:
    user_yaml["problem_type"]=result_model["modelType"]
    # else:
    #     user_yaml["problem_type"]='default'
    user_yaml["na_value"]=formData["nulltype"]
    result_project=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":currentIDs.get_current_project_id()})
    # if result_project:
    user_yaml["location"]=result_project["projectFolderPath"]
    # else:
    #     user_yaml["location"]='/'
    user_yaml["n"]=formData["modelnumber"]
    user_yaml["experimentname"]=result_project["projectName"]
    with open(os.path.join(user_yaml["location"],"autoConfig.yaml"), "w") as f:
        yaml.dump(user_yaml,f)
        f.close()
    print(user_yaml)
    automatic_model_training=auto()
    automatic_model_training.auto(os.path.join(user_yaml["location"],'autoConfig.yaml'))
    return {"Successful":"True"}


@app.get('/paths')
def return_auto_preprocesseing_metrics():
    print(settings.CONFIG_AUTO_YAML_FILE)
    print(os.path.abspath(os.path.join(settings.CONFIG_AUTO_YAML_FILE,'.yaml')))
    return {"auto-config-path":settings.CONFIG_AUTO_YAML_FILE,"data-database-folder-path":settings.DATA_DATABASE_FOLDER,"config-yaml-folder":settings.CONFIG_YAML_FOLDER}
#/auto -> make config file -> isauto, target, number of models
#make a subfolder -> address of this location send to him
#auto()
#config_id -> 
#metrics, plot files location, pickle file location, clean data location