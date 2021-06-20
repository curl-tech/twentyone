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
    return [userEntity(item) for item in entity]

def insert_one_user(id):
    pass

def find_one_user():
    pass

def edit_user():
    pass

def get_userID():
    pass

def get_user_projects():
    pass