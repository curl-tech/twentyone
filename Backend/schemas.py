from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr
from pydantic.utils import Obj
from typing import Optional
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

# class PyObjectID(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls,v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid Object')
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(tyep='string')
   

class User(BaseModel):
    # id: Optional[int]=Field(alias='_id')    #Optional[ObjectID]
    userID: int
    name: Optional[str]
    email: EmailStr
    username: str
    password: str

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True



class Project(BaseModel):
    projectID:int
    projectName:str
    rawDataPath: Optional[str]
    cleanDataPath: Optional[str]
    belongToUserID: Optional[str]
    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True

class Data(BaseModel):
    dataPath: Optional[str]
    picklePath: Optional[str]
    belongsToUserID: int
    belongsToProjectID: int

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True

class Model(BaseModel):
    modelName: Optional[str]='Default Model'
    modelTyep: Optional[str]
    wightsPath: Optional[str]
    belongsToUserID: int
    belongsToProjectID: int

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True

