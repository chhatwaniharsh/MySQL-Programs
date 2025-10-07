li=[]
def insert(eid,ename,edept,esal):
    cur.execute(f"insert into employee values({eid},'{ename}','{edept}',{esal});")
    print("Data Inserted!")

def update(eid,ename,edept,esal):
    cur.execute(f"update employee set name='{ename}',dept='{edept}',salary={esal} where id={eid}")
    print("Data Updated!")

def delete(eid):
    cur.execute(f"delete from employee where id={eid}")
    print("Data Deleted!")

def show():
    cur.execute("select * from employee;")
    for row in cur:
        print(row)

def addcol(cname,cdata,csize):
    cur.execute(f"alter table employee add {cname} {cdata}({csize});")
    print("Column Added")

def modcol(cname,cdata,csize):
    cur.execute(f"alter table employee modify {cname} {cdata}({csize});")
    print("Column Modify")
        
try:
    import mysql.connector
    conn=mysql.connector.connect(host='localhost',user='root',password='admin')
    cur=conn.cursor()

    #cur.execute('Create Database Emp;')
    print("Database Created!")

    cur.execute('Use Emp;')

    #cur.execute('create table employee(id int primary key,name varchar(30) not null,dept varchar(30) not null,salary float);')
    print("Table Created!")
    while True:
        print("--------Employee Database Menu----------")
        print("1. Insert Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. Show Record")
        print("5. Exit")
        print("6. Add Column")
        print("7. Modify Column")
        print("8. Rename Column")
        print("9. Drop Column")
        ch=int(input("Enter Choice between 1 to 5 : "))
        print("----------------------------------------")

        if ch==1:
            eid=int(input("Enter Employee ID : "))
            ename=input("Enter Employee Name : ")
            edept=input("Enter Employee Department : ")
            esal=float(input("Enter Employee Salary : "))
            insert(eid,ename,edept,esal)
        elif ch==2:
            eid=int(input("Enter Employee ID to Update : "))
            ename=input("Enter Employee Alternate Name : ")
            edept=input("Enter Employee Alternate Department : ")
            esal=float(input("Enter Employee Alternate Salary : "))
            update(eid,ename,edept,esal)
        elif ch==3:
            eid=int(input("Enter Employee ID to delete : "))
            delete(eid)
        elif ch==4:
            print("-*-*-*Employee Data*-*-*-")
            show()
            print("-*-*-*-*-*-*-*-*-*-*-*-*-")
        elif ch==5:
            print("Exiting...")
            break
        elif ch==6:
            cname=input("Enter Column Name : ")
            cdata=input("Enter Data Type : ")
            csize=int(input("Enter Data Type Size : "))
            addcol(cname,cdata,csize)
        elif ch==7:
            cname=input("Enter Column Name : ")
            cdata=input("Enter new Data Type : ")
            csize=int(input("Enter new Data Type Size : "))
            modcol(cname,cdata,csize)
        else:
            print("Please enter choice between 1 to 5 only.")
    
except mysql.connector.Error as err:
    print("Mysql Error :",err)

finally:
    conn.commit()
    cur.close()
    conn.close()
