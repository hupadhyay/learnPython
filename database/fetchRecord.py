import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", passwd="techm", db="test")

cur = db.cursor()

dbStr = 'select * from employee'
try:
    var=cur.execute(dbStr)

    if var > 0:
        results = cur.fetchall()
        for row in results:
            print(row)
        
except:
    print("got exception")
    db.rollback()

db.close()