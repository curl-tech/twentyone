def inferenceEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "belongsToUserID":item["belongsToUserID"],
        "belongsToProjectID":item["belongsToProjectID"],
        "belongsToModelID":item["belongsToModelID"],
        "newData": item["newData"],
        "results": item["results"]        
    }

def inferencesEntity(entity) -> list:
    return [inferenceEntity(item) for item in entity]


def insert_one_inference():
    pass

def find_one_inference():
    pass

def edit_inference():
    pass

def get_user_projects():
    pass