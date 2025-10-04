create database company;
use company;

create table employee(eid int,ename varchar(30),age int,department varchar(30),salary float,joining_date date,gender char(1));
insert into employee values(101,"Harsh",21,"Management",95000.5,'2022-03-30',"M");
insert into employee values(102,"Ramakant",21,"Designing",72000.4,'2024-08-17',"M");
insert into employee values(103,"XYZ",21,"ABC",45000.5,'2025-08-14',"F");

desc employee;
select * from employee;

create table department(did int,dname varchar(20),foreign key(did) references employee(eid));
insert into department values(101,"Finance"),(102,"HR");
select * from department;

set sql_safe_updates=0;
update employee set salary=78000.0 where eid=102;
delete from employee where eid=103;

alter table employee add primary key(eid);
alter table employee drop primary key;
alter table employee modify eid int;
alter table employee modify ename varchar(30) not null;

#drop table department;
#alter table department drop foreign key;
#alter table department add foreign key(did) references employee(eid) on delete cascade on update cascade;


