import os

def ResponseModel(data,message):
    return {
        "data": [data],
        "code":200,
        "message":message,
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }

def reqEntity(item) -> dict:
    return {
        "isauto":item["isauto"],
        "target":item["target"],
        "modelnumber":item["modelnumber"],
        "nulltype":item["nulltype"]
    }

def reqsEntity(entity) -> list:
    return [reqEntity(item) for item in entity]

def serialiseDict(item) -> dict:
    return {**{k:item[k] for k in item if k!='_id'}}    #To serialise the python cursor object received using pymongo's find_many and find_one method

def serialiseList(items) -> list:
    return [serialiseDict(item) for item in items]

class CurrentIDs:
    def __init__(self):
        self.userID=0
        self.projectID=0
        self.dataID=0
        self.modelID=0

    def get_current_user_id(self):
        return self.userID
    
    def get_current_project_id(self):
        return self.projectID
    
    def get_current_data_id(self):
        return self.dataID

    def get_current_model_id(self):
        return self.modelID
    
    def set_current_user_id(self,userID):
        self.userID=userID

    def set_current_project_id(self,projectID):
        self.projectID=projectID

    def set_current_data_id(self,dataID):
        self.dataID=dataID

    def set_current_model_id(self,modelID):
        self.modelID=modelID

    def print_all_ids(self):
        print("userID: ",self.userID)
        print("projectID: ",self.projectID)
        print("dataID: ",self.dataID)
        print("modelID: ",self.modelID)

class ResultsCache:
    def __init__(self):
        path=os.getcwd()
        self.cleanDataPath=path
        self.metricsPath=path
        self.pickleFilePath=path
        self.pickleFolderPath=path
        self.status=False

    def set_auto_mode_status(self,status):
        self.status=False
    
    def get_auto_mode_status(self):
        return self.status

    def set_project_folder_path(self,projectFolderPath):
        self.projectFolderPath=projectFolderPath
    
    def get_project_folder_path(self):
        return self.projectFolderPath

    def set_clean_data_path(self,cleanDataPath):
        self.cleanDataPath=cleanDataPath

    def set_metrics_path(self,metricsPath):
        self.metricsPath=metricsPath

    def set_pickle_file_path(self,pickleFilePath):
        self.pickleFilePath=pickleFilePath

    def set_pickle_folder_path(self,pickleFolderPath):
        self.pickleFolderPath=pickleFolderPath

    def get_clean_data_path(self):
        return self.cleanDataPath

    def get_metrics_path(self):
        return self.metricsPath

    def get_pickle_file_path(self):
        return self.pickleFilePath

    def get_pickle_folder_path(self):
        return self.pickleFolderPath

    def print_all_paths(self):
        print("cleanDataPath", self.cleanDataPath)
        print("metricsPath", self.metricsPath)
        print("pickleFilePath", self.pickleFilePath)
        print("pickleFolderPath", self.pickleFolderPath)
    