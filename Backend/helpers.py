def userEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "userid":item["userid"],
        "name":item["name"],
        "email":item["email"],
        "username":item["username"],
        "password":item["password"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]


def ResponseModel(data,message):
    return {
        "data": [data],
        "code":200,
        "message":message
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }