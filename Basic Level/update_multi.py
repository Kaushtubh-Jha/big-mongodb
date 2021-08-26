import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# address starts with the letter "S"
query = { "address": { "$regex": "^S" } }
updatemulti = { "$set": { "name": "Minnie" } }

x = coll.update_many(query, updatemulti)

print(x.modified_count, "data updated.")