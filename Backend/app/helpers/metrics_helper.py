import re
from Backend.app.helpers.allhelpers import serialiseDict
from Backend.app.dbclass import Database
from Backend.app.config import settings

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

def metricEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "belongsToUserID":item["belongsToUserID"],
        "belongsToProjectID":item["belongsToProjectID"],
        "belongsToModelID":item["belongsToModelID"],
        "addressOfMetricsFile": item["addressOfMetricsFile"]
    }

def metricsEntity(entity) -> list:
    return [metricEntity(item) for item in entity]


def insert_one_metric():
    pass

def get_metrics_from_modelID(modelID):
    try:
        result_metrics=Project21Database.find_one(settings.DB_COLLECTION_METRICS,{"belongsToModelID":modelID})
        result_metrics=metricEntity(result_metrics)
        if result_metrics is not None:
            if result_metrics["addressOfMetricsFile"]:
                return result_metrics["addressOfMetricsFile"]
            else:
                print("Adress of Metrics Is None")
        else:
            print("result_metrics is None")
        return '/'
    except Exception as e:
        print("An Error Occured", e)
        return '/'

def get_metrics_from_projectID(projectID):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_METRICS,{"belongsToProjectID":projectID})
        if result is not None:
            result=serialiseDict(result)
            print("Result is: ",result)
            print("Result path is ", result["addressOfMetricsFile"])
            return str(result["addressOfMetricsFile"])
    except Exception as e:
        print("An Error Occured: ", e)
    return 'result["addressOfMetricsFile"]'

def edit_metric():
    pass

def get_user_projects():
    pass