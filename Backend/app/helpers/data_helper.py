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

def get_user_projects():
    pass