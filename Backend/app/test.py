from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from app.dbclass import Database
from app.schemas import User, Project, Data, Model, Metrics
from app.helpers import userEntity, usersEntity, ResponseModel, ErrorResponseModel
from bson.json_util import dumps, ObjectId

origins=[
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000"        #Port 3000 because React app will run by default at port 3000
]

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Project21Database=Database()
Project21Database.initialise()

@app.get('/')
def home():
    return {"hello": "world"}

@app.get('/allusers',response_description="Get all users from the database.")
def get_all_users():
    return usersEntity(Project21Database.find('testcol',{'id':1}))

@app.post('/user',response_description="Update the User Collection with a new entry.")
def insert_one_user(user:User=Body(...)):
    user=jsonable_encoder(user)
    Project21Database.insert_one("user_collection",user)
    return ResponseModel(user["userID"],"Succesfully Inserted")

@app.post('/project')
def insert_one_project(project:Project=Body(...)):
    project=jsonable_encoder(project)
    Project21Database.insert_one("project_collection",project)
    return ResponseModel(project["projectID"],"Succesfully Inserted")

@app.post('/data')
def insert_one_data(data:Data=Body(...)):
    data=jsonable_encoder(data)
    Project21Database.insert_one("data_collection",data)
    return ResponseModel(data["dataPath"],"Succesfully Inserted")

@app.post('/model')
def insert_one_model(model:Model=Body(...)):
    model=jsonable_encoder(model)
    Project21Database.insert_one("model_collection",model)
    return ResponseModel(model["modelName"],"Succesfully Inserted")

@app.post('/metrics')
def insert_one_metrics(metrics:Metrics=Body(...)):
    metrics=jsonable_encoder(metrics)
    Project21Database.insert_one("metrics_collection",metrics)
    return ResponseModel(metrics["belongsToUserID"],"Succesfully Inserted")
