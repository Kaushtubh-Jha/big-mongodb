import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# delete one data
query = { "address": "Mountain 21" }
x = coll.delete_one(query)
print(x.raw_result)
print(x.deleted_count)