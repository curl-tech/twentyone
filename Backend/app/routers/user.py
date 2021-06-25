from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from Backend.app.dbclass import Database
from Backend.app.config import settings
from Backend.app.schemas import User, UpdateUser
from Backend.app.helpers.user_helper import userEntity, usersEntity
from Backend.app.helpers.allhelpers import ErrorResponseModel, ResponseModel

Project21Database=Database()
Project21Database.initialise(settings.DB_NAME)

user_router=APIRouter()

@user_router.get('/users')
def get_all_users():
    users=[]
    all_users=usersEntity(Project21Database.find(settings.DB_COLLECTION_USER,{}))
    for user in all_users:
        users.append(user)
    return users

@user_router.get('/user/{id}')
def get_one_user(id:int):
    try:
        user=userEntity(Project21Database.find_one(settings.DB_COLLECTION_USER,{"userID":id}))
    except:
        return ErrorResponseModel("An Error Occured",404,"User could not be found")
    return user

@user_router.post('/user')
def insert_one_user(user: User=Body(...)):
    user=jsonable_encoder(user)
    try:
        Project21Database.insert_one(settings.DB_COLLECTION_USER,user)
    except:
        return ErrorResponseModel("An Error Occured",404,"Could not insert User into the Collection")
    return ResponseModel(user["userID"],"Succesfully Inserted")

@user_router.put('/user/{id}')
def update_one_user(id:int,updateUser: UpdateUser=Body(...)):
    updateUser={k:v for k,v in updateUser.dict().items() if v is not None}
    result=Project21Database.find_one(settings.DB_COLLECTION_USER,{"userID":id})
    if result:
        try:
            result=Project21Database.update_one(settings.DB_COLLECTION_USER,{"userID":id},{"$set":updateUser})
            return ResponseModel(id,"Successfully Updated")
        except:
            return ErrorResponseModel("An Error Occured",404,"User could not be updated")
    return ErrorResponseModel("An Error Occured",404,"User could not be updated")

@user_router.delete('/deleteuser/{id}')
def delete_one_user(id:int):
    try:
        result=Project21Database.find_one(settings.DB_COLLECTION_USER,{"userID":id})
        if result:
            Project21Database.delete_one(settings.DB_COLLECTION_USER,{"userID":id})
        else:
            return ErrorResponseModel("An Error Occured",404,"User could not be found")
    except:
        return ErrorResponseModel("An Error Occured",404,"User could not be deleted")
    return ResponseModel(id,"Successfully Deleted")