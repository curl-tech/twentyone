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

def get_user_projects():
    pass