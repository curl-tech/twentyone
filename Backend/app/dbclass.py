from pymongo import MongoClient
from bson.json_util import dumps
from app import config

class Database(object):
    '''
    Class for initialising the MongoDB Database and functions for easy access to the DB and its collections.
    '''
    URI=config.settings.DB_URL     #Specifying the URI for the local database
    DATABASE=config.settings.DB_NAME                       #Database name

    @staticmethod
    def initialise():
        client=MongoClient(Database.URI)
        Database.DATABASE=client['testdb']       #Database name under localhost

    @staticmethod
    def insert_one(collection, data):                       #Insert data into the Collection
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def insert_many(collection, data):                      #insert multiple documents in the collection
        Database.DATABASE[collection].insert_many(data)

    @staticmethod
    def find(collection, query):                            #finds all data from the collection returns a cursor object
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):                        #finds one object from the collection the result is a dictionary
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_one(collection, query, newvalues):                   #updates the object from the collection with a query to find the object and newvalues
        Database.DATABASE[collection].update_one(query, newvalues)