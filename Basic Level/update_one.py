import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# address from "Valley 345" to "Canyon 123"
query = { "address": "Valley 345" }
udpate = { "$set": { "address": "Canyon 123" } }

coll.update_one(query, udpate)

#print "customers" after the update:
for x in coll.find():
  print(x)