from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str

class Show(BaseModel):
    name:str
    email:str
    class Config:
        orm_mode=True
     
   