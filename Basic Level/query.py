import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# find specific data
query = { "name": "DxZ" }

findquery = coll.find(query)

for x in findquery:
  print(x)