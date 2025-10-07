import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='admin')
cur=conn.cursor()
#cur.execute("Create database example")
cur.execute("Use example")
di={}
tname=input("Enter Table Name : ")
#col=input("Enter name of columns : ")
#data=input("Enter Datatype of column : ")
num=int(input("how many column add : "))
for i in range(1,num+1):
    cname=input("Enter Col Name : ")
    cdata=input("Enter Col Data Type : ")
    di.update({cname:cdata})
cur.execute(f"create table {tname} ({di})")

conn.close()

