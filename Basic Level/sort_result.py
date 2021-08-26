import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# sort result in alphabetically
findquery = coll.find().sort("name") # ascending or sort("name", 1)

for x in findquery:
  print(x)

# sort descending
findquery = coll.find().sort("name", -1) # descending

for x in findquery:
  print(x)