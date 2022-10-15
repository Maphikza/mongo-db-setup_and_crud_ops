import datetime
from pymongo import MongoClient
import os

maphikza_password = os.environ.get("mongo-db-maphikza")
cluster = f"mongodb+srv://Maphikza:{maphikza_password}@cluster0.zz6wxqr.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(cluster)

print(client.list_database_names())

db = client.test

print(db.list_collection_names())

todo1 = {
    "name": "Maphikza", "text": "Untangling3!", "status": "open",
    "tags": ["python", "testing3"], "date": datetime.datetime(2022, 9, 14, 9, 29)
}

todos = db.todos

# result = todos.insert_one(todo1)

todos2 = [{"name": "Mo", "text": "My First mention!", "status": "open",
           "tags": ["python", "analysis"], "date": str(datetime.datetime.utcnow())},
          {"name": "Tebza", "text": "My Second mention!", "status": "open",
           "tags": ["python", "marketing"], "date": str(datetime.datetime.utcnow())}]

# result = todos.insert_many(todos2)
# from bson.objectid import ObjectId
# results = todos.find({"tags": "python"})
#
# for result in results:
#     print

# print(todos.count_documents({"tags": "python"}))
# date = str(datetime.datetime(2022, 9, 15))
# results = todos.find({"date": {"$gt": date}}).sort("name")
#
# for result in results:
#     print(result)
# from bson.objectid import ObjectId
# result = todos.delete_many({"name": "Mo"})

results = todos.update_one({"tags": "python"}, {"$set": {"status": "finished"}})
