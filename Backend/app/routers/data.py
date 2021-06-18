from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from app.dbclass import Database
from app.config import settings
from app.schemas import Data, UpdateData
from app.helpers.data_helper import dataEntity, datasEntity
from app.helpers.allhelpers import ErrorResponseModel, ResponseModel

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

data_router=APIRouter()

@data_router.get('/datas')
def get_all_datas():
    datas=[]
    all_datas=datasEntity(Project21Database.find(settings.DB_COLLECTION_DATA,{}))
    for data in all_datas:
        datas.append(data)
    return datas

@data_router.get('/data/{dataID}')
def get_one_data(dataID:int):
    try:
        data=dataEntity(Project21Database.find_one(settings.DB_COLLECTION_DATA,{"dataID":dataID}))
    except:
        return ErrorResponseModel("An Error Occured",404,"Data could not be found")
    return data

@data_router.post('/data')
def insert_one_data(data: Data=Body(...)):
    data=jsonable_encoder(data)
    try:
        Project21Database.insert_one(settings.DB_COLLECTION_DATA,data)
    except:
        return ErrorResponseModel("An Error Occured",404,"Could not insert Data into the Collection")
    return ResponseModel(data["dataID"],"Succesfully Inserted")

@data_router.put('/data/{dataID}')
def update_one_data(dataID:int,updateData: UpdateData=Body(...)):
    updateData={k:v for k,v in updateData.dict().items() if v is not None}
    result=Project21Database.find_one(settings.DB_COLLECTION_DATA,{"dataID":dataID})
    if result:
        try:
            Project21Database.update_one(settings.DB_COLLECTION_DATA,{"dataID":dataID},{"$set":updateData})
            return ResponseModel(dataID,"Succesfully Updated")
        except:
            return ErrorResponseModel("An Exception error Occured",404,"Data could not be updated")
    return ErrorResponseModel("An Exception error Occured",404,"Data could not be updated")

@data_router.delete('/deletedata/{dataID}')
def delete_one_project(dataID:int):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_DATA,{"dataID":dataID})
        if result:
            Project21Database.delete_one(settings.DB_COLLECTION_DATA,{"dataID":dataID})
        else:
            return ErrorResponseModel("An Error Occured",404,"data could not be found")
    except:
        return ErrorResponseModel("An Error Occured",404,"data could not be deleted")
    return ResponseModel(dataID,"Successfully Deleted")