import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", passwd="techm", db="test")

cur = db.cursor()

dbStr = 'insert into employee (emp_id, first_name, last_name, age, salary) values (1, "himanshu", "upadhyay", 30, 500)'
try:
    var=cur.execute(dbStr)

    if var == 1:
        print("Record inserted successfully!")
        
    db.commit()
except:
    print("got exception")
    db.rollback()

db.close()