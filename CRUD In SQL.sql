create database school;
use school;

create table student1(sid int,fname varchar(30),lname varchar(30),DOB date,gender char(1),country varchar(25));
insert into student1 values(101,"Harsh","Chhatwani",'2004-03-30',"M","India");
insert into student1 values(102,"Ramakant","Chaudhari",'2004-08-17',"M","India");
insert into student1 values(103,"XYZ","ABC",'2008-12-28',"M","Austria");

desc student1;
select * from student1;
alter table student1 add fee float;
alter table student1 modify country varchar(50);
alter table student1 drop gender;
alter table student1 change lname lastname varchar(50);

set sql_safe_updates=0;
update student1 set country="Iran" where sid=102;
delete from student1 where sid=103;