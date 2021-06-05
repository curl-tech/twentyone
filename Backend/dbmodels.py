from pydantic import BaseModel
from .database import Base
#TEMPORARRY , it is to be used to make schema for mongodb
class User(Base):
    __tablename__ = 'users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    