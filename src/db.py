from pymongo import MongoClient
from mongoengine import connect

MONGO_URI = "mongodb://admin:123@localhost:27017/?authSource=admin"
DB_NAME = "bundesliga"

def get_pymongo_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db["players"]

def connect_mongoengine():
    connect(db=DB_NAME, host=MONGO_URI)