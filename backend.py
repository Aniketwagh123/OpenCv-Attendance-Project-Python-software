# import pymongo
from pymongo import MongoClient


def get_database(name,datestring,date):
    client = MongoClient('mongodb+srv://Aniketwagh123:Aniket9277@cluster0.ofr9k.mongodb.net/?retryWrites=true&w=majority')
    db = client.get_database('test-database')
    collection = db.collections
    if collection.count_documents({"Name":name,"date":date})==0:
        collection.insert_one({"Name":name,"Time":datestring,"date":date})
    return

# get_database("Name","Aniket")
