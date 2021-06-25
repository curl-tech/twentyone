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
"""
yaml format - 

config.py - problem_type -> str            #regression, clasi
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