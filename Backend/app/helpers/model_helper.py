from Backend.app.helpers.allhelpers import serialiseDict
from Backend.app.dbclass import Database
from Backend.app.config import settings
import random

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

def modelEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "modelID":item["modelID"],
        "modelName":item["modelName"],
        "modelType":item["modelType"],
        "picklePath":item["picklePath"],
        "belongsToUserID":item["belongsToUserID"],
        "belongsToProjectID":item["belongsToProjectID"],
        "belongsToDataID":item["belongsToDataID"]
    }

def modelsEntity(entity) -> list:
    return [modelEntity(item) for item in entity]

def create_model_id():
    id = random.randint(10000,99999)
    result=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":id})
    if result:
        id=create_model_id()
    return id

def get_pickle_file_path(modelID):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID})
        result=serialiseDict(result)
        if result is not None:
            return result["picklePath"]
        else:
            return '/'
    except:
        print("An error occured while retreiving picklePath from the Model Collection")
        return '/'

def insert_one_model():
    pass

def find_one_model():
    pass

def edit_model():
    pass

def get_modelID():
    pass

def get_user_projects():
    pass