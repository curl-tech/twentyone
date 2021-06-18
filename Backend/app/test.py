from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from app.dbclass import Database
from app.config import settings
from app.routers.user import user_router
from app.routers.project import project_router

origins=settings.CORS_ORIGIN

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router, tags=["user"])
app.include_router(project_router, tags=["project"])

Project21Database=Database()
Project21Database.initialise(settings.DB_COLLECTION_USER)

@app.get('/')
def home():
    return {"hello": "world"}

@app.get('/serverstatus')
def server_status():
    return {"serverstatus": "working"}

@app.on_event("startup")
async def startup_mongodb_client():
    Project21Database.initialise(settings.DB_NAME)


@app.on_event("shutdown")
async def shutdown_mongodb_client():
    Project21Database.close()

# @app.post('/project')
# def insert_one_project(project:Project=Body(...)):
#     project=jsonable_encoder(project)
#     Project21Database.insert_one("project_collection",project)
#     return ResponseModel(project["projectID"],"Succesfully Inserted")

# @app.post('/data')
# def insert_one_data(data:Data=Body(...)):
#     data=jsonable_encoder(data)
#     Project21Database.insert_one("data_collection",data)
#     return ResponseModel(data["dataPath"],"Succesfully Inserted")

# @app.post('/model')
# def insert_one_model(model:Model=Body(...)):
#     model=jsonable_encoder(model)
#     Project21Database.insert_one("model_collection",model)
#     return ResponseModel(model["modelName"],"Succesfully Inserted")

# @app.post('/metrics')
# def insert_one_metrics(metrics:Metrics=Body(...)):
#     metrics=jsonable_encoder(metrics)
#     Project21Database.insert_one("metrics_collection",metrics)
#     return ResponseModel(metrics["belongsToUserID"],"Succesfully Inserted")
