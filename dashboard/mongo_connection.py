import pymongo

def database_access():
    client = pymongo.MongoClient("mongodb://dev:dev@localhost:27017/eassy_connection")
    database = client['eassy_connection']
    return database