import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# return 5 data
result = coll.find().limit(1)

# print the result:
for x in result:
  print(x)