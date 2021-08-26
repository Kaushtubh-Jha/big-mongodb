import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# check if a collection exist
print(dbname.list_collection_names())

# check for "employee" collection
allcollt = dbname.list_collection_names()
if "employee" in allcollt:
  print("The collection exists.")

# collection will not create until unless you will insert into collection