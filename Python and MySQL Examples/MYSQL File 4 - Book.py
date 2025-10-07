import mysql.connector
def insert(bid,name,auth):
    cur.execute(f"insert into book values({bid},'{name}','{auth}');")
    print("Data Inserted Successfully")

def update(bid,name):
    cur.execute(f"update book set name='{name}' where id={bid};")
    print("Data Updated Successfully")

def delete(bid):
    cur.execute(f"delete from book where id={bid};")
    print("Data deleted Successfully")

def show():
    cur.execute("Select * from book;")
    for r in cur:
        print(r)

try:
    
    mydb=mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='admin')
    cur=mydb.cursor()
    #print(mydb.connection_id)

    #cur.execute("Create Database abc1")
    print("Database Created Successfully")

    cur.execute("Use abc1")
    #cur.execute("Create table book(id int,name varchar(32),author varchar(32));")
    print("Table Created Successfully")

    while True:
        print("-------Book Database Menu-------")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Show Data")
        print("5. Exit")
        ch=int(input("Enter your choice : "))
        print("-----------------------------------")

        if ch==1:
            bid=int(input("Enter Book ID. : "))
            name=input("Enter Book Name : ")
            auth=input("Enter Book Author : ")
            insert(bid,name,auth)
        elif ch==2:
            bid=int(input("Enter Book ID. : "))
            name=input("Enter Book Name : ")
            update(bid,name)
        elif ch==3:
            bid=int(input("Enter Book ID. : "))
            delete(bid)
        elif ch==4:
            print("*****Book Data*****")
            show()
            print("**********************")
        elif ch==5:
            print("Exiting Program")
            break
        else:
            print("Inalid Choice Please enter a number between 1 to 5")

except mysql.connector.Error as err:
    print("MYSQL Error :",err)

finally:
    mydb.commit()
    cur.close()
    mydb.close()
