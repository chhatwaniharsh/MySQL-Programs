import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='admin')
#print(mydb)
print(mydb.connection_id)
cur=mydb.cursor()
#cur.execute("Create database mydb1")
