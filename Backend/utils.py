import os
import shutil
from app.helpers.project_helper import merge_project_path


def findCleanData():
    pass     #path string returned

def modelPickleFile():
    pass     #pickle file returned

def generate_project_folder(projectName,train):
    try:
        with open("rawdata.csv","wb") as buffer:
            shutil.copyfileobj(train.file,buffer)
        path=os.getcwd()
        newpath=os.path.abspath(os.path.join(path,os.pardir))
        newpath=newpath+'/Database/'+merge_project_path(projectName)+'/data/'
        os.makedirs(newpath)
        shutil.move(path+'/rawdata.csv',newpath)
        return {"Success":True, "Path":newpath+'rawdata.csv'}
    except:
        return {"Success":False,"Error": "File could not be saved. Folder creation unsuccessful"}


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