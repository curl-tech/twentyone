import re
from traceback import print_tb
from Backend.app.helpers.allhelpers import serialiseDict
from Backend.app.config import settings
from Backend.utils import Project21Database


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


def insert_one_data():
    pass

def find_one_data():
    pass

def edit_data():
    pass

def get_dataID():
    pass

def get_clean_data_path(dataID):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_DATA,{"dataID":dataID})
        result=serialiseDict(result)
        if result is not None:
            return result["cleanDataPath"]
        else:
            return '/'
    except:
        print("An error occured while retreiving cleanDataPath from Data Collection")

def get_user_projects():
    pass