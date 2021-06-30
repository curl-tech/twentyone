from Backend.app.helpers.allhelpers import serialiseDict
from Backend.app.config import settings
import random

def modelEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "modelID":item["modelID"],
        "modelName":item["modelName"],
        "modelType":item["modelType"],
        "pickleFolderPath":item["pickleFolderPath"],
        "pickleFilePath": item["pickleFilePath"],
        "belongsToUserID":item["belongsToUserID"],
        "belongsToProjectID":item["belongsToProjectID"],
        "belongsToDataID":item["belongsToDataID"]
    }

def modelsEntity(entity) -> list:
    return [modelEntity(item) for item in entity]

def create_model_id(Project21Database):
    id = random.randint(10000,99999)
    result=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":id})
    if result:
        id=create_model_id()
    return id

def get_pickle_file_path(modelID,Project21Database):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID})
        if result is not None:
            result=serialiseDict(result)
            return result["pickleFilePath"]
            # if result["pickleFilePath"] is not None:
            #     return result["pickleFilePath"]
        else:
            print("result is none")
            return '/'
    except Exception as e:
        print("An error occured while retreiving pickleFilePath from the Model Collection")
        print("Error: ",e)
        return '/'