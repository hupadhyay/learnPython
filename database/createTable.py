import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", passwd="techm", db="test")

cur = db.cursor()

dbStr1 = 'drop table if exists employee'

dbStr2 = 'create table employee (emp_id int primary key, first_name text, last_name text, age int, salary float)'

cur.execute(dbStr1)

help(cur.execute)

cur.execute(dbStr2)

db.close()