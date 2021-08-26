import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# make advanced queries we can use modifiers as values in the query object
query = { "address": { "$gt": "S" } }

findquery = coll.find(query)

for x in findquery:
  print(x)
  