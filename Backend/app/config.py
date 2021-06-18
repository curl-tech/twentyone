from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = "Project 21"
    DEBUG_MODE: bool=True

class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

class DatabaseSettings(BaseSettings):
    DB_URI: str = "mongodb://localhost:27017"       #MongoDB running by default at port 27017 of localhost
    DB_NAME : str = "Project21Database"
    DB_COLLECTION_USER: str = "user_collection"
    DB_COLLECTION_PROJECT: str = "project_collection"
    DB_COLLECTION_DATA: str = "data_collection"
    DB_COLLECTION_MODEL: str = "model_collection"
    DB_COLLECTION_METRICS: str = "metrics_collection"
    DB_COLLECTION_INFERENCE: str = "inference_collection"

class Settings(CommonSettings,ServerSettings,DatabaseSettings):
    CORS_ORIGIN=[
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000"        #React app running by default at port 3000
    ]
    pass

settings=Settings()