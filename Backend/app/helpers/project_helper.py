import random
from Backend.app.config import settings
from Backend.app.helpers.allhelpers import serialiseDict


def get_raw_data_path(projectID,Project21Database):
    try:  
        result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":projectID})
        result=serialiseDict(result)
        if result is not None:
            return result["rawDataPath"]   #path string returned
        else:
            return ''
    except Exception as e:
        print("An Error Occured: ",e)
        print("An Error Occured While Retreiving rawDataPath from the Project Collection")
        return ''

def get_project_type(projectID,Project21Database):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":projectID})
        result=serialiseDict(result)
        if result is not None:
            return result["projectType"]
        else:
            return ''
    except Exception as e:
        print("An Error Occured: ",e)
        print("An Error Occured while retreiving projectType from the Project Collection")
        return ''

# def get_project_id(userID,Project21Database):
#     try:
#         result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"belongsToUserID":userID})
#         result=serialiseDict(result)
#         if result is not None:
#             return result["projectID"]
#         else:
#             return 0
#     except:
#         print("An Error Occured While Retreiving projectID from the Project Collection")

def merge_project_path(projectName):
    projectPath = projectName+"_"+"%0.16d"%random.randint(0,9999999999999999)
    return projectPath

def create_project_id(Project21Database):
    id = random.randint(10000,99999)
    result = Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":id})
    if result:
        id=create_project_id()
    return id