import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

for x in coll.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)