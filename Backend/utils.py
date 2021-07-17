import os
import random
import shutil
import yaml
from yaml.loader import SafeLoader
from Backend.app.config import settings
from Backend.app.helpers.project_helper import merge_project_path, get_raw_data_path, get_project_type
from Backend.app.helpers.allhelpers import CurrentIDs, serialiseDict

def generate_random_id():
    """
    Generates a 5 digit random number from 10000 to 99999
    """
    return random.randint(10000,99999)

def generate_project_folder(projectName,trainFileStream):
    """
    Generates a project folder with the name projectName_16digitrandomnumber
    ...
    Parameters
    ----------
    projectName: str
    trainFileStream: UploadFile type
    Returns
    -------
    dict: Success, RawDataPath, ProjectFolderPath
        or Success, Error
    """
    try:
        newpath=os.path.join(os.getcwd(),"Database",merge_project_path(projectName),'raw_data')
        if(not os.path.exists(newpath)):
            os.makedirs(newpath)
        with open(os.path.join(newpath,"raw_data.csv"),"wb") as buffer:
            shutil.copyfileobj(trainFileStream.file,buffer)
        return {"Success":True, "RawDataPath":os.path.abspath(os.path.join(newpath,"raw_data.csv")),"ProjectFolderPath":os.path.abspath(os.path.join(newpath,os.pardir))}
    except:
        return {"Success":False,"Error": "File could not be saved. Folder creation unsuccessful"}


def generate_project_auto_config_file(projectID,currentIDs,formData,Project21Database):
    """
    Returns the auto config file generated for the project
    ...
    Parameters
    ----------
    projectID: int
    currentIDs: obj
    formData: obj
    Project21Databse: obj
    
    Returns
    -------
    tuple: path, randomID, problemType
    """
    user_yaml=yaml.load(open(settings.CONFIG_AUTO_YAML_FILE),Loader=SafeLoader)
    random_id=generate_random_id()
    user_yaml["id"]=random_id
    user_yaml["raw_data_address"]=get_raw_data_path(projectID,Project21Database)
    user_yaml["target_col_name"]=formData["target"]
    user_yaml["na_value"]=formData["nulltype"]
    user_yaml["n"]=formData["modelnumber"]
    user_yaml["problem_type"]=get_project_type(projectID,Project21Database)
    if(user_yaml["problem_type"]=='clustering'):
        user_yaml["clusteringType"]=formData["clusteringType"]
    # try:
    #     result_model=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":currentIDs.get_current_model_id()})
    #     result_model=serialiseDict(result_model)
    #     if result_model is not None:
    #         user_yaml["problem_type"]=result_model["modelType"]
    #     else:
    #         user_yaml["problem_type"]='default'
    # except:
    #     print("Unable to Update User's Project's AutoConfig File")

    try:
        result_project=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":projectID})
        result_project=serialiseDict(result_project)
        if result_project is not None:
            user_yaml["location"]=os.path.join(result_project["projectFolderPath"],'run'+str(random_id))
            user_yaml["experimentname"]=result_project["projectName"]
        else:
            user_yaml["location"]='/'
            user_yaml["experimentname"]='default'
    except:
        print("Unable to Update User's Project's Config File")
    if(not os.path.exists(user_yaml["location"])):
        os.makedirs(user_yaml["location"])
    with open(os.path.join(user_yaml["location"],"autoConfig.yaml"), "w") as f:
        yaml.dump(user_yaml,f)
        f.close()
    
    return os.path.join(user_yaml["location"],'autoConfig.yaml'), random_id , user_yaml["problem_type"]




def generate_project_manual_config_file(projectID,preprocessJSONFormData,Project21Database):
    """
    
    """
    location="/"
    random_id=generate_random_id()
    try:
        result_project=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":projectID})
        result_project=serialiseDict(result_project)
        if result_project is not None:
            location=os.path.join(result_project["projectFolderPath"],'run'+str(random_id))
    except:
        print("Unable to Update User's Project's Config File")
    if(not os.path.exists(location)):
        os.makedirs(location)
    with open(os.path.join(location,"preprocess_config.yaml"), "w") as f:
        yaml.dump(preprocessJSONFormData,f)
        f.close()
    
    return os.path.join(location,'preprocess_config.yaml'), random_id , result_project["projectType"], location