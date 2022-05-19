from pymongo import MongoClient


def get_database():
    import pymongo
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test-database']
    collection = db.collections
    # posts = db.posts
    post_id = collection.insert_one({"p":1}).inserted_id
    print(post_id)
    # collection.update_one({"p":   1} , {$set:{"p":12}})


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()