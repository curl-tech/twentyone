import os
import shutil
from fastapi import FastAPI, Form
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import File
from fastapi.responses import JSONResponse, FileResponse
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.routers.user import user_router
from Backend.app.routers.project import project_router
from Backend.app.routers.data import data_router
from Backend.app.routers.model import model_router
from Backend.app.routers.metrics import metrics_router
from Backend.app.routers.inference import inference_router
from Backend.app.helpers.allhelpers import CurrentIDs, ResultsCache, serialiseDict, serialiseList
from Backend.app.helpers.project_helper import create_project_id
from Backend.app.helpers.data_helper import get_clean_data_path
from Backend.app.helpers.metrics_helper import get_metrics
from Backend.app.helpers.model_helper import create_model_id, get_pickle_file_path
from Backend.app.schemas import FormData, Inference
from Backend.utils import generate_project_folder, generate_project_auto_config_file
from Files.auto import Auto
from Files.autoreg import AutoReg
from Files.plot import plot
from Files.inference import Inference

origins=settings.CORS_ORIGIN

app=FastAPI()

app.include_router(user_router, tags=["User Collection CRUD Operations"])
app.include_router(project_router, tags=["Project Collection CRUD Operations"])
app.include_router(data_router, tags=["Data Collection CRUD Operations"])
app.include_router(model_router,tags=["Model Collection CRUD Operations"])
app.include_router(metrics_router,tags=["Metrics Collection CRUD Operations"])
app.include_router(inference_router,tags=["Inference Collection CRUD Operations"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Project21Database=Database()
currentIDs=CurrentIDs()
resultsCache=ResultsCache()
currentIDs.set_current_user_id(101)


@app.get('/')
def home(): 
    return JSONResponse({"Hello": "World","serverStatus":"Working"})

@app.on_event("startup")
def startup_mongodb_client():
    Project21Database.initialise(settings.DB_NAME)
    try:
        currentIDs.set_current_user_id(101)
        Project21Database.insert_one(settings.DB_COLLECTION_USER,{
                "userID":101,
                "name": "John Doe",
                "email": "johndoe@email.com",
                "username": "TheJohnDoe",
                "password": "password@Super@Secure",
                "listOfProjects": []
            })
        resultsCache.set_auto_mode_status(False)
    except Exception as e:
        print("An Error Occured: ",e)
        print("Duplicate Key Error can be ignored safely")
    pass

@app.on_event("shutdown")
def shutdown_mongodb_client():
    Project21Database.close()

@app.post('/create',tags=["Auto Mode"])
def create_project(projectName:str=Form(...),mtype:str=Form(...),train: UploadFile=File(...)):
    inserted_projectID=0
    Operation=generate_project_folder(projectName,train)
    if Operation["Success"]:
        try:
            inserted_projectID=create_project_id(Project21Database)
            # inserted_modelID=create_model_id(Project21Database)
            currentIDs.set_current_project_id(inserted_projectID)
            # currentIDs.set_current_model_id(inserted_modelID)
            resultsCache.set_project_folder_path(Operation["ProjectFolderPath"])
            Project21Database.insert_one(settings.DB_COLLECTION_PROJECT,{
                "projectID":inserted_projectID,
                "projectName":projectName,
                "rawDataPath":Operation["RawDataPath"],
                "projectFolderPath":Operation["ProjectFolderPath"],
                "belongsToUserID": currentIDs.get_current_user_id(),
                "listOfDataIDs":[],
                "autoConfigFileLocation": None,
                "plotsPath": "",
                "projectType": mtype
                })
            # Project21Database.insert_one(settings.DB_COLLECTION_MODEL,{
            #     "modelID": inserted_modelID,
            #     "modelName": "Default Model",
            #     "modelType": mtype,
            #     "belongsToUserID": currentIDs.get_current_user_id(),
            #     "belongsToProjectID": inserted_projectID
            # })
            try:
                result=Project21Database.find_one(settings.DB_COLLECTION_USER,{"userID":currentIDs.get_current_user_id()})
                if result is not None:
                    result=serialiseDict(result)
                    if result["listOfProjects"] is not None:
                        newListOfProjects=result["listOfProjects"]
                        newListOfProjects.append(inserted_projectID)
                        Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":result["userID"]},{"$set":{"listOfProjects":newListOfProjects}})
                    else:
                        Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":result["userID"]},{"$set":{"listOfProjects":[inserted_projectID]}})
            except Exception as e:
                print("An Error occured: ",e)
                return JSONResponse({"File Received": "Success", "Project Folder":"Success", "Database Update":"Partially Successful"})
        except Exception as e:
            print("An Error occured: ",e)
            return JSONResponse({"File Received": "Success","Project Folder":"Success","Database Update":"Failure"})
        return JSONResponse({"userID":currentIDs.get_current_user_id(),"projectID":inserted_projectID})
    else:
        return JSONResponse(Operation["Error"])

@app.post('/auto',tags=["Auto Mode"])
def start_auto_preprocessing(formData:FormData):
    formData=dict(formData)
    projectAutoConfigFileLocation, dataID, problem_type = generate_project_auto_config_file(formData["projectID"],currentIDs,formData,Project21Database)
    resultsCache.set_auto_mode_status(False)
    if(problem_type=='regression'):
        automatic_model_training=AutoReg()
        Operation=automatic_model_training.auto(projectAutoConfigFileLocation)
    else:
        automatic_model_training=Auto()
        Operation=automatic_model_training.auto(projectAutoConfigFileLocation)
        
    if Operation["Successful"]:
        try:
            Project21Database.insert_one(settings.DB_COLLECTION_DATA,{
                "dataID": dataID,
                "cleanDataPath": Operation["cleanDataPath"],
                "target": formData["target"],
                "belongsToUserID": currentIDs.get_current_user_id(),
                "belongsToProjectID": formData["projectID"]
            })
            currentIDs.set_current_data_id(dataID)
            Project21Database.insert_one(settings.DB_COLLECTION_MODEL,{
                "modelID": dataID,
                "modelName": "Default Name",
                "modelType": problem_type,
                "pickleFolderPath": Operation["pickleFolderPath"],
                "pickleFilePath": Operation["pickleFilePath"],
                "belongsToUserID": formData["userID"],
                "belongsToProjectID": formData["projectID"],
                "belongsToDataID": dataID
            })
            Project21Database.insert_one(settings.DB_COLLECTION_METRICS,{
                "belongsToUserID": formData["userID"],
                "belongsToProjectID": formData["projectID"],
                "belongsToModelID": dataID,
                "addressOfMetricsFile": Operation["metricsLocation"]
            })
            try:
                result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":formData["projectID"]})
                result=serialiseDict(result)
                if result is not None:
                    if result["listOfDataIDs"] is not None:
                        newListOfDataIDs=result["listOfDataIDs"]
                        newListOfDataIDs.append(dataID)
                        Project21Database.update_one(settings.DB_COLLECTION_PROJECT,{"projectID":result["projectID"]},{
                            "$set":{
                                "listOfDataIDs":newListOfDataIDs,
                                "autoConfigFileLocation": projectAutoConfigFileLocation,
                                "isAuto": formData["isauto"]
                                }
                            })
                    else:
                        Project21Database.update_one(settings.DB_COLLECTION_PROJECT,{"projectID":result["projectID"]},{
                            "$set":{
                                "listOfDataIDs":[dataID],
                                "autoConfigFileLocation": projectAutoConfigFileLocation,
                                "isAuto": formData["isauto"]
                                }
                            })
            except Exception as e:
                print("An Error occured: ",e)
                return JSONResponse({"Auto": "Success", "Database Insertion":"Success", "Project Collection Updation": "Unsuccessful"})
        except Exception as e:
            print("An Error occured: ",e)
            return JSONResponse({"Auto": "Success", "Database Insertion":"Failure", "Project Collection Updation": "Unsuccessful"})
        
        resultsCache.set_clean_data_path(Operation["cleanDataPath"])
        resultsCache.set_metrics_path(Operation["metricsLocation"])
        resultsCache.set_pickle_file_path(Operation["pickleFilePath"])
        resultsCache.set_pickle_folder_path(Operation["pickleFolderPath"])
        resultsCache.set_auto_mode_status(True)
        return JSONResponse({"Successful":"True", "userID": currentIDs.get_current_user_id(), "projectID": formData["projectID"], "dataID":dataID, "modelID": dataID})
    else:
        return JSONResponse({"Successful":"False"})


@app.get('/getMetrics/{projectID}/{modelID}',tags=["Auto Mode"])
def get_auto_generated_metrics(projectID:int,modelID:int):
    metricsFilePath=get_metrics(projectID,modelID,Project21Database)
    if (os.path.exists(metricsFilePath)):
        return FileResponse(metricsFilePath,media_type="text/csv", filename="metrics.csv")
    return {"Error": "Metrics File not found at path"}


@app.get('/downloadClean/{dataID}',tags=["Auto Mode"])
def download_clean_data(dataID:int):
    path=get_clean_data_path(dataID,Project21Database)       #Have to put dataID here
    if(os.path.exists(path)):
        return FileResponse(path,media_type="text/csv",filename="clean_data.csv")     #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"Clean Data File not found at path"}


@app.get('/downloadPickle/{modelID}',tags=["Auto Mode"])
def download_pickle_file(modelID:int):
    path=get_pickle_file_path(modelID,Project21Database)       #Have to put modelID here
    if(os.path.exists(path+'.pkl')):
        print("Path: ",path)
        return FileResponse(path+'.pkl',media_type="application/octet-stream",filename="model.pkl")   #for this we need aiofiles to be installed. Use pip install aiofiles
    return {"Error":"File not found at path"}
# #     myfile=open(path,mode='rb')
#     return StreamingResponse(myfile,media_type="text/csv")    #for streaming files instead of uploading them


@app.get('/getPlots/{projectID}',tags=["Auto Mode"])        #To-DO: make the plots appear in each sub directory and see the config file according to the userID, projectID and dataID given
def get_plots(projectID:int):       #check if it already exists - change location address
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"projectID":projectID})
        if result is not None:
            result=serialiseDict(result)
            if result["autoConfigFileLocation"] is not None:
                plotFilePath=plot(result["autoConfigFileLocation"]) #plot function requires the auto config file
                try:
                    Project21Database.update_one(settings.DB_COLLECTION_PROJECT,{"projectID":projectID},{
                        "$set": {
                            "plotsPath": plotFilePath
                        }
                    })
                except Exception as e:
                    print("An Error occured while storing the plot path into the project collection")
                return FileResponse(plotFilePath,media_type='text/html',filename='plot.html')
    except Exception as e:
        print("An Error Occured: ",e)
        return JSONResponse({"Plots": "Not generated"})


@app.get('/getAllProjects',tags=["Auto Mode"])
def get_all_project_details(userID:int):
    # try:
    #     result=Project21Database.find_one(settings.DB_COLLECTION_PROJECT,{"belongsToUserID":userID})
    #     if result is not None:
    #         listOfDataIDs=result["listOfDataIDs"]
    #         for dataID in listOfDataIDs:
                
    pass


@app.post('/doInference',tags=["Auto Mode"])
def get_inference_results(projectID:int=Form(...),modelID:int=Form(...),inferenceDataFile: UploadFile=File(...)):
    newDataPath='/'
    pickleFilePath='/'
    path='/'
    inferenceDataResultsPath='/'
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_MODEL,{"modelID":modelID,"belongsToProjectID":projectID})
        if result is not None:
            result=serialiseDict(result)
            if result["pickleFilePath"] is not None:
                pickleFilePath=result["pickleFilePath"]
            if result["pickleFolderPath"] is not None:
                projectRunPath=os.path.join(result["pickleFolderPath"],os.pardir)
                path=os.path.join(projectRunPath,"inference_data")
                if(not os.path.exists(path)):
                    os.makedirs(path)
                newDataPath=os.path.join(path,'inference_data.csv')
            
            with open(newDataPath,"wb") as buffer:
                shutil.copyfileobj(inferenceDataFile.file,buffer)

            inference=Inference()
            inferenceDataResultsPath=inference.inference(pickleFilePath,newDataPath,path,True)
            Project21Database.insert_one(settings.DB_COLLECTION_INFERENCE,{
                "newData": newDataPath,
                "results": inferenceDataResultsPath,
                "belongsToUserID": currentIDs.get_current_user_id(),
                "belongsToProjectID": projectID,
                "belongsToModelID": modelID
            })
            if os.path.exists(inferenceDataResultsPath):
                print({"Metrics Generation":"Successful"})
                return FileResponse(inferenceDataResultsPath,media_type="text/csv",filename="inference.csv")
    except Exception as e:
        print("An error occured: ", e)
        print("Unable to find model from model Collection")
        return JSONResponse({"Metrics Generation":"Failed"})
    



# @app.websocket("/ws")
# async def training_status(websocket: WebSocket):
#     print("Connecting to the Frontend...")
#     await websocket.accept()
#     # while (not resultsCache.get_auto_mode_status()):
#     try:
#         data={
#             "Successful":"False",
#             "Status": "Model Running"
#         }
#         if (resultsCache.get_auto_mode_status()):
#             data={
#             "Successful":"True",
#             "Status": "Model Successfully Created",
#             "userID": currentIDs.get_current_user_id(),
#             "projectID": currentIDs.get_current_project_id(),
#             "dataID":currentIDs.get_current_data_id(),
#             "modelID": currentIDs.get_current_model_id()
#             }
#             await websocket.send_json(data)
#         data2= await websocket.receive_text()  #Can be used to receive data from frontend
#         print(data2)
#         await websocket.send_json(data) #Can be used to return data to the frontend
#     except Exception as e:
#         print("Error: ",e)
#         # break
#     print("Websocket connection closing...")