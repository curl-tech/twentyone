def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "otherid":item["id"],
        "name":item["name"],
        "email":item["email"],
        "password":item["username"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]