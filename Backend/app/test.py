import os
from fastapi import FastAPI, Body, Request, Form
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import File
from fastapi.responses import StreamingResponse
from starlette.responses import FileResponse
from app.dbclass import Database
from app.config import settings
from app.routers.user import user_router
from app.routers.project import project_router
from app.routers.data import data_router
from app.routers.model import model_router
from app.routers.metrics import metrics_router
from app.routers.inference import inference_router
from app.helpers.allhelpers import reqsEntity, reqEntity
from app.helpers.project_helper import create_project_id, get_project_id, get_raw_data_path
from app.helpers.model_helper import create_model_id
from utils import generate_project_folder
from app.schemas import FormData

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
# Project21Database.initialise(settings.DB_COLLECTION_USER)

@app.get('/')
def home():
    return {"hello": "world"}

@app.get('/serverstatus')
def server_status():
    return {"serverstatus": "working"}

@app.on_event("startup")
def startup_mongodb_client():
    Project21Database.initialise(settings.DB_NAME)

@app.on_event("shutdown")
def shutdown_mongodb_client():
    Project21Database.close()

@app.post('/create')
async def create_project(projectName:str=Form(...),mtype:str=Form(...),train: UploadFile=File(...)):
    operation=generate_project_folder(projectName,train)
    if operation["Success"]:
        Project21Database.insert_one(settings.DB_COLLECTION_PROJECT,{
            "projectID":create_project_id(),
            "projectName":projectName,
            "rawDataPath":operation["Path"],
            "belongsToUserID": 101
            })
        Project21Database.insert_one(settings.DB_COLLECTION_MODEL,{
            "modelID": create_model_id(),
            "modelName": "Default Model",
            "modelType": mtype,
            "belongsToUserID": 101,
            "belongsToProjectID": get_project_id(101)
        })
        return {"File Received Successfully": "Project Folder Creation Successful"}
    else:
        return operation["Error"]

#2nd api call
@app.get('/file')
def file():
    path=get_raw_data_path(25763)       #Have to put projectID here
    myfile=open(path,mode='rb')
    return StreamingResponse(myfile,media_type="text/csv")

@app.get('/file-download')
def file_download():
    path=get_raw_data_path(25763)       #Have to put projectID here
    if(os.path.exists(path)):
        return FileResponse(path,media_type="text/csv")     #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"File not found at path"}

@app.post('/auto')
async def auto(formData:FormData):
    print(formData)
    return {"Successful":"True"}
#/auto -> make config file -> modeltype, target, number of models, raw data address
#make a subfolder -> address of this location send to him
#auto()
#config_id -> 
#metrics, plot files location, pickle file location, clean data location