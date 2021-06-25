from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.schemas import Metrics
from Backend.app.helpers.metrics_helper import metricEntity, metricsEntity
from Backend.app.helpers.allhelpers import ErrorResponseModel, ResponseModel

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

metrics_router=APIRouter()

@metrics_router.get('/metrics')
def get_all_metrics():
    metrics=[]
    all_metrics=metricsEntity(Project21Database.find(settings.DB_COLLECTION_METRICS,{}))
    for data in all_metrics:
        metrics.append(data)
    return metrics

@metrics_router.get('/metrics/{belongsToModelID}')
def get_one_metrics(belongsToModelID:int):
    try:
        metrics=metricEntity(Project21Database.find_one(settings.DB_COLLECTION_METRICS,{"belongsToModelID":belongsToModelID}))
    except:
        return ErrorResponseModel("An Error Occured",404,"Metrics could not be found")
    return metrics

@metrics_router.post('/metrics')
def insert_one_metrics(metrics: Metrics=Body(...)):
    metrics=jsonable_encoder(metrics)
    try:
        Project21Database.insert_one(settings.DB_COLLECTION_METRICS,metrics)
    except:
        return ErrorResponseModel("An Error Occured",404,"Could not insert Metrics into the Collection")
    return ResponseModel(metrics["belongsToModelID"],"Succesfully Inserted")

@metrics_router.delete('/deletemetrics/{belongsToModelID}')
def delete_one_project(belongsToModelID:int):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_METRICS,{"belongsToModelID":belongsToModelID})
        if result:
            Project21Database.delete_one(settings.DB_COLLECTION_METRICS,{"belongsToModelID":belongsToModelID})
        else:
            return ErrorResponseModel("An Error Occured",404,"Metrics could not be found")
    except:
        return ErrorResponseModel("An Error Occured",404,"Metrics could not be deleted")
    return ResponseModel(belongsToModelID,"Successfully Deleted")