from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from dbclass import Database
from schemas import User, Project, Data, Model, Metrics
from helpers import userEntity, usersEntity, ResponseModel, ErrorResponseModel
from bson.json_util import dumps, ObjectId
from pydantic import BaseModel

app=FastAPI()
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
