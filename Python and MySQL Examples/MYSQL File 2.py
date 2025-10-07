import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='admin')
cur=mydb.cursor()
print(mydb.connection_id)

#cur.execute("Create Database abc1")
print("Database Created Successfully")

cur.execute("Use abc1")
#cur.execute("Create table stud(id int,name varchar(32));")
print("Table Created Successfully")

#cur.execute("insert into stud values(1,'Harsh');")
#cur.execute("insert into stud values(2,'Ramakant');")
#cur.execute("insert into stud values(3,'Veer');")
print("Data Inserted Successfully")

#cur.execute("update stud set name='Raj' where id=2;")
print("Data Updated Successfully")

#cur.execute("delete from stud where id=2;")
print("Data deleted Successfully")

cur.execute("Select * from stud;")
for r in cur:
    print(r)

mydb.commit()
cur.close()
mydb.close()
