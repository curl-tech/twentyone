from Backend.app.helpers.allhelpers import serialiseDict
from Backend.app.config import settings

def dataEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "dataID":item["dataID"],
        "cleanDataPath":item["cleanDataPath"],
        "target":item["target"],
        "belongsToUserID":item["belongsToUserID"],
        "belongsToProjectID":item["belongsToProjectID"]
    }

def datasEntity(entity) -> list:
    return [dataEntity(item) for item in entity]


def get_clean_data_path(dataID,Project21Database):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_DATA,{"dataID":dataID})
        result=serialiseDict(result)
        if result is not None:
            return result["cleanDataPath"]
        else:
            return '/'
    except:
        print("An error occured while retreiving cleanDataPath from Data Collection")
