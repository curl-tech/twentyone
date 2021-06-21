import os
from fastapi import FastAPI, Body, Request, Form
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import File
from app.dbclass import Database
from app.config import settings
from app.routers.user import user_router
from app.routers.project import project_router
from app.routers.data import data_router
from app.routers.model import model_router
from app.routers.metrics import metrics_router
from app.routers.inference import inference_router
from app.helpers.allhelpers import reqsEntity, reqEntity
from app.helpers.project_helper import create_projectID, create_project_id
from app.helpers.model_helper import create_modelID
from utils import generate_project_folder

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
Project21Database.initialise(settings.DB_COLLECTION_USER)

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
            "modelID": create_modelID(),
            "modelName": "Default Model",
            "modelType": mtype,
            "belongsToUserID": 101,
            "belongsToProjectID": create_project_id(),      #to be changed to get_project_id(userID)
            "belongsToDataID": 2
        })
        return {"File Received Successfully": "Project Folder Creation Successful"}
    else:
        return operation["Error"]

#2nd api call
@app.get('/auto')
def auto():
    return {"Parent Directory":os.path.abspath(os.path.join(os.getcwd(),os.pardir))}

@app.post('/auto')
async def auto(isauto:str=Form(...),target:str=Form(...),modelnumber:str=Form(...),nulltype:str=Form(...)):
    print(isauto)
    print(target)
    print(modelnumber)
    print(nulltype)
    return {"Successful":"True"}
#/auto -> make config file -> modeltype, target, number of models, raw data address
#make a subfolder -> address of this location send to him
#auto()
#config_id -> 
#metrics, plot files location, pickle file location, clean data location