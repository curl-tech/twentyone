from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.schemas import InferenceCollection
from Backend.app.helpers.allhelpers import ErrorResponseModel, ResponseModel, serialiseDict, serialiseList

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

inference_router=APIRouter()

@inference_router.get('/inferences')
def get_all_inferences():
    inferences=[]
    all_inferences=serialiseList(Project21Database.find(settings.DB_COLLECTION_INFERENCE,{}))
    for data in all_inferences:
        inferences.append(data)
    return inferences

@inference_router.get('/inference/{belongsToModelID}')
def get_one_inference(belongsToModelID:int):
    try:
        inference=serialiseDict(Project21Database.find_one(settings.DB_COLLECTION_INFERENCE,{"belongsToModelID":belongsToModelID}))
    except:
        return ErrorResponseModel("An Error Occured",404,"Inference could not be found")
    return inference

@inference_router.post('/inference')
def insert_one_inference(inference: InferenceCollection=Body(...)):
    inference=jsonable_encoder(inference)
    try:
        Project21Database.insert_one(settings.DB_COLLECTION_INFERENCE,inference)
    except:
        return ErrorResponseModel("An Error Occured",404,"Could not insert Inference into the Collection")
    return ResponseModel(inference["belongsToModelID"],"Succesfully Inserted")

@inference_router.delete('/deleteinference/{belongsToModelID}')
def delete_one_project(belongsToModelID:int):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_INFERENCE,{"belongsToModelID":belongsToModelID})
        if result:
            Project21Database.delete_one(settings.DB_COLLECTION_INFERENCE,{"belongsToModelID":belongsToModelID})
        else:
            return ErrorResponseModel("An Error Occured",404,"Inference could not be found")
    except:
        return ErrorResponseModel("An Error Occured",404,"Inference could not be deleted")
    return ResponseModel(belongsToModelID,"Successfully Deleted")