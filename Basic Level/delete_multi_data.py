import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# delete multi data using regex
query = { "address": {"$regex": "^S"} }

x = coll.delete_many(query)

print(x.deleted_count, "data deleted.")