import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", passwd="techm", db="test")

cur = db.cursor()

dbStr = 'delete from employee where emp_id=1'
try:
    var=cur.execute(dbStr)

    if var > 0:
        print('Record deleted')
    
    db.commit() 
except:
    print("got exception")
    db.rollback()

db.close()