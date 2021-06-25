import pymongo
from pymongo import MongoClient
from Backend.app import config

class Database(object):
    '''
    Class for initialising the MongoDB Database and functions for easy access to the DB and its collections.
    '''
    URI=config.settings.DB_URI     #Specifying the URI for the local database
    DATABASE=None                       #Database name

    @staticmethod
    def initialise(dbname):
        client=MongoClient(Database.URI)
        Database.DATABASE=client[dbname]       #Database name under localhost
        Database.DATABASE[config.settings.DB_COLLECTION_USER].create_index([('userID',pymongo.ASCENDING)],unique=True)
        Database.DATABASE[config.settings.DB_COLLECTION_PROJECT].create_index([('projectID',pymongo.ASCENDING)],unique=True)
        Database.DATABASE[config.settings.DB_COLLECTION_DATA].create_index([('dataID',pymongo.ASCENDING)],unique=True)
        Database.DATABASE[config.settings.DB_COLLECTION_MODEL].create_index([('modelID',pymongo.ASCENDING)],unique=True)
        

    @staticmethod
    def close():                                #To Close the Database connection
        client=MongoClient(Database.URI)
        client.close()

    @staticmethod
    def insert_one(collection, data):                       #Insert data into the Collection
        inserted_id=Database.DATABASE[collection].insert_one(data).inserted_id
        return inserted_id

    @staticmethod
    def insert_many(collection, data):                      #insert multiple documents in the collection
        inserted_ids=Database.DATABASE[collection].insert_many(data).inserted_ids
        return inserted_ids

    @staticmethod
    def find(collection, query):                            #finds all data from the collection returns a cursor object
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):                    #finds one object from the collection the result is a dictionary
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_one(collection, query, newvalues):                   #updates the object from the collection with a query to find the object and newvalues
        Database.DATABASE[collection].update_one(query, newvalues)

    @staticmethod
    def delete_one(collection,query):                       #delete one object from the collection
        Database.DATABASE[collection].delete_one(query)