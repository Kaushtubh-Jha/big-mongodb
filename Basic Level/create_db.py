import pymongo

#  create a database "basicleveldb"
connection = pymongo.MongoClient("mongodb://localhost:27017/")
dbname = connection["local"]

# check if a database exist by listing all databases in you system
print(connection.list_database_names())

# check a specific database
alldbs = connection.list_database_names()
if "local" in alldbs:
  print("The database exists.")


# db will not create until unless you will insert into db