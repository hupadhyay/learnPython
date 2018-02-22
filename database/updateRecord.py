import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", passwd="techm", db="test")

cur = db.cursor()

dbStr = 'update employee set age=age+1 where emp_id=1'
try:
    var=cur.execute(dbStr)

    if var > 0:
        print('Record updated.')
        
    db.commit()
except:
    print("got exception")
    db.rollback()

db.close()