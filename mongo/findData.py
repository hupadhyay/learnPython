from pymongo import MongoClient

client = MongoClient('localhost', 27017)

myDb = client['workdb']

myTable = myDb['movies'];

data = myTable.find()

# Getting of mongoDB Records

for record in data:
    print(f'data from mongodb = {record["title"]}')

# Getting of names of movies
for record in data:
    print(f'data from mongodb = {record["title"]}')

