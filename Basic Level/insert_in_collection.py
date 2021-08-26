import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# insert data inside "employee" collection
data = { "name": "DxZ", "address": "Dark Road 6 Feet" }

insrt = coll.insert_one(data)

# inserted_id holds the id of the inserted document
print(insrt.inserted_id)