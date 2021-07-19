from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.schemas import Model, UpdateModel
from Backend.app.helpers.allhelpers import ErrorResponseModel, ResponseModel, serialiseDict, serialiseList

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

model_router=APIRouter()

@model_router.get('/models')
def get_all_models():
    models=[]
    all_models=serialiseList(Project21Database.find(settings.DB_COLLECTION_MODEL,{}))
    for data in all_models:
        models.append(data)
    return models

@model_router.get('/model/{modelID}')
def get_one_model(modelID:int):
    try:
        model=serialiseDict(Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID}))
    except:
        return ErrorResponseModel("An Error Occured",404,"Model could not be found")
    return model

@model_router.post('/model')
def insert_one_model(model: Model=Body(...)):
    model=jsonable_encoder(model)
    try:
        Project21Database.insert_one(settings.DB_COLLECTION_MODEL,model)
    except:
        return ErrorResponseModel("An Error Occured",404,"Could not insert Model into the Collection")
    return ResponseModel(model["modelID"],"Succesfully Inserted")

@model_router.put('/model/{modelID}')
def update_one_model(modelID:int,updateModel: UpdateModel=Body(...)):
    updateModel={k:v for k,v in updateModel.dict().items() if v is not None}
    result=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID})
    if result:
        try:
            Project21Database.update_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID},{"$set":updateModel})
            return ResponseModel(modelID,"Succesfully Updated")
        except:
            return ErrorResponseModel("An Exception error Occured",404,"Model could not be updated")
    return ErrorResponseModel("An Exception error Occured",404,"Model could not be updated")

@model_router.delete('/deletemodel/{modelID}')
def delete_one_project(modelID:int):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID})
        if result:
            Project21Database.delete_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID})
        else:
            return ErrorResponseModel("An Error Occured",404,"data could not be found")
    except:
        return ErrorResponseModel("An Error Occured",404,"data could not be deleted")
    return ResponseModel(modelID,"Successfully Deleted")