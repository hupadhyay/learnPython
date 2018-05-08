from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)

myDb = client['workdb']

table= myDb['movies']

try:
    table.insert(json.loads('{"title":"Aag"}'));
    table.insert(json.loads('{"title":"deewana"}'));
    print('Data inserted successfully!');
except :
    print('Exception occurs while inserting data into mongo DB')
