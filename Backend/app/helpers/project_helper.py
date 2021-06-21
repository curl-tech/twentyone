import random


def projectEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "projectID":item["projectID"],
        "projectName":item["projectName"],
        "rawDataPath":item["rawDataPath"],
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

def get_projectID():
    pass

def create_projectID(projectName):
    projectID = projectName+"_"+"%0.16d"%random.randint(0,9999999999999999)
    return projectID

def create_project_id():
    return random.randint(10000,99999)


def get_user_projects():
    pass