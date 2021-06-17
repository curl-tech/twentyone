from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr
from typing import Optional
from bson.json_util import ObjectId

class User(BaseModel):
    userID: int = Field(...)
    name: Optional[str]
    email: EmailStr=Field(...)
    username: str=Field(...)
    password: str=Field(...)

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        


class Project(BaseModel):
    projectID:int=Field(...)
    projectName:Optional[str]
    rawDataPath: Optional[str]
    belongToUserID: Optional[str]
    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True

class Data(BaseModel):
    dataId: int=Field(...)
    cleanDataPath: Optional[str]
    target: Optional[str]
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True

class Model(BaseModel):
    modelName: Optional[str]='Default Model'
    modelType: Optional[str]
    modelId: int
    belongsToUserID: int
    belongsToProjectID: int
    belongsToDataID: int
    picklePath: Optional[str]

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True

class Metrics(BaseModel):
    belongsToUserID: int
    belongsToProjectID: int
    belongsToModelID: int
    addressofYamlFile: str

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True

class Inference(BaseModel):
    newData: str    #address
    results: str    #yaml file
    
