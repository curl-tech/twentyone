import os
import re
from fastapi import FastAPI, Form, WebSocket
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import File
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
from starlette.types import Receive
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.routers.user import user_router
from Backend.app.routers.project import project_router
from Backend.app.routers.data import data_router
from Backend.app.routers.model import model_router
from Backend.app.routers.metrics import metrics_router
from Backend.app.routers.inference import inference_router
from Backend.app.helpers.allhelpers import CurrentIDs, serialiseDict, serialiseList
from Backend.app.helpers.project_helper import create_project_id
from Backend.app.helpers.data_helper import get_clean_data_path
from Backend.app.helpers.model_helper import create_model_id, get_pickle_file_path
from Backend.app.schemas import FormData
from Backend.utils import generate_project_folder, generate_project_auto_config_file
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
        currentIDs.set_current_user_id(101)
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
                if result is not None:
                    result=serialiseDict(result)
                    if result["listOfProjects"]:
                        newListOfProjects=result["listOfProjects"]
                        newListOfProjects.append(inserted_projectID)
                        Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":result["userID"]},{"$set":{"listOfProjects":newListOfProjects}})
                    else:
                        Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":result["userID"]},{"$set":{"listOfProjects":[inserted_projectID]}})
            except:
                return JSONResponse({"File Received": "Success", "Project Folder":"Success", "Database Update":"Partially Successful"})
        except:
            return JSONResponse({"File Received": "Success","Project Folder":"Success","Database Update":"Failure"})
        return JSONResponse({"File Received": "Success", "Project Folder":"Success", "Database Update":"Success"})
    else:
        return JSONResponse(operation["Error"])

@app.post('/auto')
def start_auto_preprocessing(formData:FormData):
    formData=dict(formData)
    projectAutoConfigFileLocation=generate_project_auto_config_file(currentIDs,formData,)
    automatic_model_training=auto()
    automatic_model_training.auto(projectAutoConfigFileLocation)
    #receive clean_data.csv path and update data_collection
    #send metrics to frontend
    return JSONResponse({"Successful":"True"})

@app.get('/auto')
def return_auto_generated_metrics():
    return JSONResponse({"metrics":"path/to/metrics.csv"})

@app.get('/downloadClean')
def download_clean_data():
    print("current user id: ",currentIDs.get_current_user_id())
    path=get_clean_data_path(currentIDs.get_current_data_id())       #Have to put dataID here
    if(os.path.exists(path)):
        return FileResponse(path,media_type="text/csv")     #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"File not found at path"}

@app.get('/downloadPickle')
def file_download():
    path=get_pickle_file_path(currentIDs.get_current_model_id())       #Have to put modelID here
    if(os.path.exists(path)):
        return FileResponse(path,media_type="text/csv")     #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"File not found at path"}
#     myfile=open(path,mode='rb')
#     return StreamingResponse(myfile,media_type="text/csv")    #for streaming files instead of uploading them

@app.websocket("/ws")
async def training_status(websocket: WebSocket):
    print("Connecting to the Frontend...")
    await websocket.accept()
    while True:
        try:
            await websocket.receive_json()  #Can be used to receive data from frontend
            resp={"Status":"ModelRunning"}  
            await websocket.send_json(resp) #Can be used to return data to the frontend
        except Exception as e:
            print("Error: ",e)
            break
    print("Websocket connection closing...")