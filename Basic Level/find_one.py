import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# create the collection
coll = dbname["employee"]

# find one data
x = coll.find_one(5) # give id to return that id data, if no id given it will return first data
print(x)
