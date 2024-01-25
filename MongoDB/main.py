import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["local"]
mydb["student"].insert_one({"name": "John", "regno": "211FA04563","course":"B.Tech","branch":"CSE",'email':"jhon@gmail.com"})
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
