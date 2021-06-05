from typing import Optional
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from bson import ObjectId
from pydantic.fields import Field
from pydantic.networks import EmailStr
from pydantic.utils import Obj

class PyObjectID(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid Object')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(tyep='string')
   

class User(BaseModel):
    id: Optional[PyObjectID]=Field(alias='_id')
    name: str
    email: EmailStr
    username: str

    class Config:
        allow_population_by_field_name=True
        arbitraty_types_allowed=True
        json_encoders={
            ObjectId:str
        }
        schema_extra={
            "id":1,
            "name": "John Doe",
            "email": "johndoe@gmail.com",
            "username": "JohnDoe"
        }

class Show(BaseModel):
    name:Optional[str]
    email:Optional[str]
    class Config:
        orm_mode=True
        arbitrary_types_allowed=True
        json_encoders={ ObjectId: str}
        schema_extra={
            "name":"Jane Doe",
            "email":"janedoe@gmail.com"
        }

