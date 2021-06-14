#from schemas import User, Show
from pymongo import MongoClient
import pprint

class Database(object):
    '''
    Class for initialising the MongoDB Database and functions for easy access to the DB and its collections.
    '''
    URI='mongodb://127.0.0.1:27017'     #Specifying the URI for the local database
    DATABASE=None                       #Database name

    @staticmethod
    def initialise():
        client=MongoClient(Database.URI)
        Database.DATABASE=client['newcollection']       #Collection name under the DB

    @staticmethod
    def insert_one(collection, data):                       #Insert data into the Collection
        Database.DATABASE[collection].insert_one(data)

    def find(self,collection, query):                            #finds all data from the collection returns a cursor object
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):                        #finds one object from the collection the result is a dictionary
        return Database.DATABASE[collection].find_one(query)


Project21Database=Database()
Project21Database.initialise()

data={
    "id":1,
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "username": "JohnDoe"
}
Project21Database.insert_one('newcollection',data)

myresults=Project21Database.find('newcollection',{'id':1})
mylist=[]
for doc in myresults:
    mylist.append(doc)
    print(doc)

print('This is our list ',mylist)