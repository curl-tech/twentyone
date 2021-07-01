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
