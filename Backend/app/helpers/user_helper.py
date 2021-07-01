from Backend.app.helpers.allhelpers import serialiseDict


def userEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "userID":item["userID"],
        "name":item["name"],
        "email":item["email"],
        "username":item["username"],
        "listOfProjects":item["listOfProjects"]
    }

def usersEntity(entity) -> list:
    return [serialiseDict(item) for item in entity]
