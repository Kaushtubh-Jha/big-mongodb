import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# pass an empty query object to the delete_many() to delete all
x = coll.delete_many({})

print(x.deleted_count, " documents deleted.")