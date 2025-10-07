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

def insert(rn,name):
    cur.execute(f"insert into stud values({rn},'{name}');")
    print("Data Inserted Successfully")

def update(rn,name):
    cur.execute(f"update stud set name='{name}' where id={rn};")
    print("Data Updated Successfully")

def delete(rn):
    cur.execute(f"delete from stud where id={rn};")
    print("Data deleted Successfully")

def show():
    cur.execute("Select * from stud;")
    for r in cur:
        print(r)

while True:
    print("-------Student Database Menu-------")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Show Data")
    print("5. Exit")
    ch=int(input("Enter your choice : "))
    print("-----------------------------------")

    if ch==1:
        rn=int(input("Enter Roll No. : "))
        name=input("Enter Name : ")
        insert(rn,name)
    elif ch==2:
        rn=int(input("Enter Roll No. to update : "))
        name=input("Enter alternate Name : ")
        update(rn,name)
    elif ch==3:
        rn=int(input("Enter Roll No. to delete : "))
        delete(rn)
    elif ch==4:
        print("*****Student Data*****")
        show()
        print("**********************")
    elif ch==5:
        print("Exiting Program")
        break
    else:
        print("Inalid Choice Please enter a number between 1 to 5")


mydb.commit()
cur.close()
mydb.close()
