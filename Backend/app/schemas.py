from pydantic import BaseModel
from pydantic.errors import PydanticErrorMixin
from pydantic.fields import Field
from pydantic.networks import EmailStr
from typing import List, Optional
from bson.json_util import ObjectId

class User(BaseModel):
    userID: int=Field(...)
    name: Optional[str]
    email: Optional[EmailStr]
    username: str=Field(...)
    password: str=Field(...)
    listOfProjects: Optional[List[int]]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "userID":101,
                "name": "John Doe",
                "email": "johndoe@email.com",
                "username": "TheJohnDoe",
                "password": "password@Super@Secure",
                "listOfProjects": [45,43,22]
            }
        }

class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    listOfProjects: Optional[List[int]]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "name": "John Doe",
                "email": "johndoe@email.com",
                "listOfProjects": [45,43,22]
            }
        }

class Project(BaseModel):
    projectID:int=Field(...)
    projectName:Optional[str]
    rawDataPath: Optional[str]
    belongsToUserID: int=Field(...)
    listOfDataIDs: Optional[List[int]]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "projectID": 45,
                "projectName": "Boston Housing",
                "rawDataPath": "/path/to/data/rawfile.csv",
                "belongsToUserID": 101,
                "listOfDataIDs": [2,4]
            }
        }

class UpdateProject(BaseModel):
    projectName:Optional[str]
    rawDataPath: Optional[str]
    listOfDataIDs: Optional[List[int]]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "projectName": "Boston Housing",
                "rawDataPath": "/path/to/data/rawfile.csv",
                "listOfDataIDs": [2,4]
            }
        }

class Data(BaseModel):
    dataID: int=Field(...)
    cleanDataPath: Optional[str]
    target: Optional[str]
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "dataID": 2,
                "cleanDataPath": "/path/to/data/cleanfile.csv",
                "target": "TargetColumnName",
                "belongsToUserID": 101,
                "belongsToProjectID": 45
            }
        }

class UpdateData(BaseModel):
    cleanDataPath: Optional[str]
    target: Optional[str]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "cleanDataPath": "/path/to/data/cleanfile.csv",
                "target": "TargetColumnName"
            }
        }


class Model(BaseModel):
    modelId: int=Field(...)
    modelName: Optional[str]='Default Model'
    modelType: Optional[str]
    picklePath: Optional[str]
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)
    belongsToDataID: int=Field(...)

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "modelID": 13,
                "modelName": "Linear Regression",
                "modelType": "Regression",
                "picklePath": "/path/to/pickle/data/model.pkl",
                "belongsToUserID": 101,
                "belongsToProjectID": 45,
                "belongsToDataID": 2
            }
        }

class UpdateModel(BaseModel):
    modelName: Optional[str]='Default Model'
    modelType: Optional[str]
    picklePath: Optional[str]

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "modelName": "Linear Regression",
                "modelType": "Regression",
                "picklePath": "/path/to/pickle/data/model.pkl"
            }
        }

class Metrics(BaseModel):
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)
    belongsToModelID: int=Field(...)
    addressOfYamlFile: str=Field(...)

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "belongsToUserID": 101,
                "belongsToProjectID": 45,
                "belongsToModelID": 13,
                "addressOfYamlFile": "/path/to/file.yaml"
            }
        }

class Inference(BaseModel):
    newData: Optional[str]    #address
    results: Optional[str]    #yaml file
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)
    belongsToModelID: int=Field(...)

    class Config:
        allow_population_by_fiel_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "newData": "/path/to/new/inference/data.csv",
                "results": "/path/to/results",
                "belongsToUserID": 101,
                "belongsToProjectID": 45,
                "belongsToModelID": 13
            }
        }