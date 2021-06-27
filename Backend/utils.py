import os
import random
import shutil
import yaml
from yaml.loader import SafeLoader
from Backend.app.config import settings
from Backend.app.helpers.project_helper import merge_project_path, get_raw_data_path
from Backend.app.dbclass import Database
from Backend.app.helpers.allhelpers import serialiseDict

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

def findCleanData():
    pass     #path string returned

def modelPickleFile():
    pass     #pickle file returned

def generate_random_id():
    return random.randint(10000,99999)

def generate_project_folder(projectName,train):
    try:
        newpath=os.path.join(os.getcwd(),"Database",merge_project_path(projectName),'raw_data')
        os.makedirs(newpath)
        with open(os.path.join(newpath,"raw_data.csv"),"wb") as buffer:
            shutil.copyfileobj(train.file,buffer)
        return {"Success":True, "RawDataPath":os.path.abspath(os.path.join(newpath,"raw_data.csv")),"ProjectFolderPath":os.path.abspath(os.path.join(newpath,os.pardir))}
    except:
        return {"Success":False,"Error": "File could not be saved. Folder creation unsuccessful"}


def generate_project_auto_config_file(currentIDs,formData):
    user_yaml=yaml.load(open(settings.CONFIG_AUTO_YAML_FILE),Loader=SafeLoader)
    random_id=currentIDs.get_current_model_id()
    user_yaml["id"]=random_id
    user_yaml["raw_data_address"]=get_raw_data_path(currentIDs.get_current_project_id())
    user_yaml["target_col_name"]=formData["target"]
    user_yaml["na_value"]=formData["nulltype"]
    user_yaml["n"]=formData["modelnumber"]
    
    try:
        result_model=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":currentIDs.get_current_model_id()})
        result_model=serialiseDict(result_model)
        if result_model is not None:
            user_yaml["problem_type"]=result_model["modelType"]
        else:
            user_yaml["problem_type"]='default'
    except:
        print("Unable to Update User's Project's AutoConfig File")

    try:
        result_project=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":currentIDs.get_current_project_id()})
        result_project=serialiseDict(result_project)
        if result_project is not None:
            user_yaml["location"]=os.path.join(result_project["projectFolderPath"],'run'+str(random_id))
            user_yaml["experimentname"]=result_project["projectName"]
        else:
            user_yaml["location"]='/'
            user_yaml["experimentname"]='default'
    except:
        print("Unable to Update User's Project's Config File")
    # if (os.path.exists(os.path.join(user_yaml["location"],"autoConfig.yaml")) is False):
    #     os.makedirs(user_yaml["location"])
    os.mkdir(user_yaml["location"])
    with open(os.path.join(user_yaml["location"],"autoConfig.yaml"), "w") as f:
        yaml.dump(user_yaml,f)
        f.close()
    
    return os.path.join(user_yaml["location"],'autoConfig.yaml'), random_id


"""
yaml format - 

config.py - type? -> str            #regression, clasi
config.raw_data_address - > str     #path/to/file.csv
config.target_column_name -> str    #name of column        
config.na_valies - >                #frontend will give  
config.experiment_name ->           #frontend
config.id ->                    #project created -> will change the id for each run
config.location ->              #place where the pickle files are to be stored for the particular project
config.n ->                     #from frontend - number of models that the user wants (ex: top 5)
config.isAuto -> bool          #from frontend

frontend - json format it will be sent ^



path
project001/model001/file001

function (...) - 'filepath/data/test.csv'
target variable


from myfolder.myfile import myfunc
"""