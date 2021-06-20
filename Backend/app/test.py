from fastapi import FastAPI, Body, Request, Form
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import File
import shutil
from app.dbclass import Database
from app.config import settings
from app.routers.user import user_router
from app.routers.project import project_router
from app.routers.data import data_router
from app.routers.model import model_router
from app.routers.metrics import metrics_router
from app.routers.inference import inference_router

origins=settings.CORS_ORIGIN

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router, tags=["user"])
app.include_router(project_router, tags=["project"])
app.include_router(data_router, tags=["data"])
app.include_router(model_router,tags=["model"])
app.include_router(metrics_router,tags=["metrics"])
app.include_router(inference_router,tags=["inference"])

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

@app.get('/create')
def create():
    return "Working fine";
@app.post('/create')
async def create(projectName:str=Form(...),mtype:str=Form(...),train: UploadFile=File(...)):
    
    print(train)
    # print(uploadedFile.filename)
    # print(uploadedFile.content_type)
    # print(uploadedFile.file)
    # response=uploadedFile.read()
    # with open("destination.csv","wb") as buffer:
    #     shutil.copyfileobj(uploadedFile.file,buffer)
    # projectName=createModel["projectName"]
    # train=createModel["train"] #send columns name
    # modelType=createModel["modelType"]
    #folder create - database folder
    #project_name_random16digitnumber
    #subfolder data
    #train file stored here
    #store address of train file in db
    #store modeltype in db
    return {"file received":"succesfully"}

#2nd api call
@app.get('/auto')
def auto():
    return 'working';
@app.post('/auto')
async def auto(req:Request):
    return req.body;
#/auto -> make config file -> modeltype, target, number of models, raw data address
#make a subfolder -> address of this location send to him
#auto()
#config_id -> 
#metrics, plot files location, pickle file location, clean data location