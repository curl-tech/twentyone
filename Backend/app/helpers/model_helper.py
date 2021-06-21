import random

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

def create_modelID():
    return random.randint(10000,99999)

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