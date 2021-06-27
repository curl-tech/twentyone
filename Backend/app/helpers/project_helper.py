import re
from Backend.app.helpers.allhelpers import serialiseDict
import random
from Backend.app.dbclass import Database
from Backend.app.config import settings

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

def projectEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "projectID":item["projectID"],
        "projectName":item["projectName"],
        "rawDataPath":item["rawDataPath"],
        "projectFolderPath": item["projectFolderPath"],
        "belongsToUserID":item["belongsToUserID"],
        "listOfDataIDs":item["listOfDataIDs"]
    }

def projectsEntity(entity) -> list:
    return [projectEntity(item) for item in entity]


def insert_one_project():
    pass

def find_one_project():
    pass

def edit_project():
    pass

def get_raw_data_path(projectID):
    try:  
        result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":projectID})
        result=serialiseDict(result)
        if result is not None:
            return result["rawDataPath"]   #path string returned
        else:
            return '/'
    except:
        print("An Error Occured While Retreiving rawDataPath from the Project Collection")
        return '/'

def get_project_id(userID):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"belongsToUserID":userID})
        result=serialiseDict(result)
        if result is not None:
            return result["projectID"]
        else:
            return 0
    except:
        print("An Error Occured While Retreiving projectID from the Project Collection")

def merge_project_path(projectName):
    projectPath = projectName+"_"+"%0.16d"%random.randint(0,9999999999999999)
    return projectPath

def create_project_id():
    id = random.randint(10000,99999)
    result = Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":id})
    if result:
        id=create_project_id()
    return id


def get_user_projects():
    pass