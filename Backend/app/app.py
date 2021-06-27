import os
from fastapi import FastAPI, Form, WebSocket
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import File
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.routers.user import user_router
from Backend.app.routers.project import project_router
from Backend.app.routers.data import data_router
from Backend.app.routers.model import model_router
from Backend.app.routers.metrics import metrics_router
from Backend.app.routers.inference import inference_router
from Backend.app.helpers.allhelpers import CurrentIDs, ResultsCache, serialiseDict, serialiseList
from Backend.app.helpers.project_helper import create_project_id
from Backend.app.helpers.data_helper import get_clean_data_path
from Backend.app.helpers.metrics_helper import get_metrics_from_modelID, get_metrics_from_projectID
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
resultsCache=ResultsCache()
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
    except Exception as e:
        print("An Error Occured: ",e)
        print("Duplicate Key Error can be ignored safely")
        pass

@app.on_event("shutdown")
def shutdown_mongodb_client():
    Project21Database.close()

@app.post('/create')
def create_project(projectName:str=Form(...),mtype:str=Form(...),train: UploadFile=File(...)):
    Operation=generate_project_folder(projectName,train)
    if Operation["Success"]:
        try:
            inserted_projectID=create_project_id()
            inserted_modelID=create_model_id()
            currentIDs.set_current_project_id(inserted_projectID)
            currentIDs.set_current_model_id(inserted_modelID)
            Project21Database.insert_one(settings.DB_COLLECTION_PROJECT,{
                "projectID":inserted_projectID,
                "projectName":projectName,
                "rawDataPath":Operation["RawDataPath"],
                "projectFolderPath":Operation["ProjectFolderPath"],
                "belongsToUserID": currentIDs.get_current_user_id(),
                "listOfDataIDs":[]
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
                    if result["listOfProjects"] is not None:
                        newListOfProjects=result["listOfProjects"]
                        newListOfProjects.append(inserted_projectID)
                        Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":result["userID"]},{"$set":{"listOfProjects":newListOfProjects}})
                    else:
                        Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":result["userID"]},{"$set":{"listOfProjects":[inserted_projectID]}})
            except Exception as e:
                print("An Error occured: ",e)
                return JSONResponse({"File Received": "Success", "Project Folder":"Success", "Database Update":"Partially Successful"})
        except Exception as e:
            print("An Error occured: ",e)
            return JSONResponse({"File Received": "Success","Project Folder":"Success","Database Update":"Failure"})
        return JSONResponse({"File Received": "Success", "Project Folder":"Success", "Database Update":"Success"})
    else:
        return JSONResponse(Operation["Error"])

@app.post('/auto')
def start_auto_preprocessing(formData:FormData):
    formData=dict(formData)
    projectAutoConfigFileLocation, dataID = generate_project_auto_config_file(currentIDs,formData,)
    automatic_model_training=auto()
    Operation=automatic_model_training.auto(projectAutoConfigFileLocation)

    if Operation["Successful"]:
        try:
            Project21Database.insert_one(settings.DB_COLLECTION_DATA,{
                "dataID": dataID,
                "cleanDataPath": Operation["cleanDataPath"],
                "target": formData["target"],
                "belongsToUserID": currentIDs.get_current_user_id(),
                "belongsToProjectID": currentIDs.get_current_project_id()
            })
            currentIDs.set_current_data_id(dataID)
            Project21Database.update_one(settings.DB_COLLECTION_MODEL,{"modelID":currentIDs.get_current_model_id()},{
                "$set": {
                    "belongsToDataID": dataID,
                    "pickleFolderPath": Operation["pickleFolderPath"],
                    "pickleFilePath": Operation["pickleFilePath"],
                }
            })
            Project21Database.insert_one(settings.DB_COLLECTION_METRICS,{
                "belongsToUserID": currentIDs.get_current_user_id(),
                "belongsToProjectID": currentIDs.get_current_project_id(),
                "belongsToModelID": currentIDs.get_current_model_id(),
                "addressOfMetricsFile": Operation["metricsLocation"]
            })
            try:
                result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":currentIDs.get_current_project_id()})
                result=serialiseDict(result)
                if result is not None:
                    if result["listOfDataIDs"] is not None:
                        newListOfDataIDs=result["listOfDataIDs"]
                        newListOfDataIDs.append(currentIDs.get_current_data_id())
                        Project21Database.update_one(settings.DB_COLLECTION_PROJECT,{"projectID":result["projectID"]},{"$set":{"listOfDataIDs":newListOfDataIDs}})
                    else:
                        Project21Database.update_one(settings.DB_COLLECTION_USER,{"projectID":result["projectID"]},{"$set":{"listOfProjects":[currentIDs.get_current_data_id()]}})
            except Exception as e:
                print("An Error occured: ",e)
                return JSONResponse({"Auto": "Success", "Database Insertion":"Success", "Project Collection Updation": "Unsuccessful"})
        except Exception as e:
            print("An Error occured: ",e)
            return JSONResponse({"Auto": "Success", "Database Insertion":"Failure", "Project Collection Updation": "Unsuccessful"})
        
        resultsCache.set_clean_data_path(Operation["cleanDataPath"])
        resultsCache.set_metrics_path(Operation["metricsLocation"])
        resultsCache.set_pickle_file_path(Operation["pickleFilePath"])
        resultsCache.set_pickle_folder_path(Operation["pickleFolderPath"])
        return JSONResponse({"Successful":"True", "Operation": resultsCache.get_clean_data_path()})
    else:
        return JSONResponse({"Successful":"False"})

@app.get('/auto/{projectID}')
def return_auto_generated_metrics(projectID):
    metricsFilePath=get_metrics_from_projectID(projectID)
    if (os.path.exists(str(metricsFilePath))):
        metricsFile=open(metricsFilePath)
        return FileResponse(metricsFile,media_type="text/csv")
    return {"metrics": "path/to/metrics.csv"}
    # metricsFilePath=resultsCache.get_metrics_path()
    # if os.path.exists(metricsFilePath):
    #     metricsFile=open(metricsFilePath,mode='rb')
    #     return StreamingResponse(metricsFile,media_type="text/csv")
    # return JSONResponse({"Error":"Metrics Not Found"})

@app.get('/downloadClean/{dataID}')
def download_clean_data(dataID):
    path=get_clean_data_path(dataID)       #Have to put dataID here
    if(os.path.exists(path)):
        return FileResponse(path,media_type="text/csv")     #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"File not found at path"}

@app.get('/downloadPickle/{modelID}')
def file_download(modelID):
    path=get_pickle_file_path(modelID)       #Have to put modelID here
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