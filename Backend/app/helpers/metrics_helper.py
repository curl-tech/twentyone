def metricEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "belongsToUserID":item["belongsToUserID"],
        "belongsToProjectID":item["belongsToProjectID"],
        "belongsToModelID":item["belongsToModelID"],
        "addressOfYamlFile": item["addressOfYamlFile"]
    }

def metricsEntity(entity) -> list:
    return [metricEntity(item) for item in entity]


def insert_one_metric():
    pass

def find_one_metric():
    pass

def edit_metric():
    pass

def get_user_projects():
    pass