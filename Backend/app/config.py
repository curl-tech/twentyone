from pydantic import BaseSettings
import os

class CommonSettings(BaseSettings):
    APP_NAME: str = "Project 21"
    DEBUG_MODE: bool=True

class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000
    CORS_ORIGIN=[
    "http://localhost:3000",        #For Cross Origin Requests to be allowed as React runs on port 3000
    ]

class DatabaseSettings(BaseSettings):
    DB_URI: str = "mongodb://localhost:27017"       #MongoDB running by default at localhost port 27017
    DB_NAME : str = "Project21Database"
    DB_COLLECTION_USER: str = "user_collection"
    DB_COLLECTION_PROJECT: str = "project_collection"
    DB_COLLECTION_DATA: str = "data_collection"
    DB_COLLECTION_MODEL: str = "model_collection"
    DB_COLLECTION_METRICS: str = "metrics_collection"
    DB_COLLECTION_INFERENCE: str = "inference_collection"

class Settings(CommonSettings,ServerSettings,DatabaseSettings):
    DATA_DATABASE_FOLDER: str = os.path.abspath(os.path.join(os.getcwd(),'Database')) 
    CONFIG_AUTO_YAML_FILE: str = os.path.abspath(os.path.join(os.getcwd(),'Files','config','autoConfig.yaml'))
    CONFIG_YAML_FOLDER: str = os.path.abspath(os.path.join(os.getcwd(),'Files','config'))
    CONFIG_PREPROCESS_YAML_FILE: str =os.path.abspath(os.path.join(os.getcwd(),'Files','config','preprocess_config.yaml'))
    CONFIG_MODEL_YAML_FILE: str=os.path.abspath(os.path.join(os.getcwd(),'Files','config','model.yaml'))
    pass

settings=Settings()