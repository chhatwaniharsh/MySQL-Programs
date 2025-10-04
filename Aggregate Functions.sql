create database h1;
use h1;

create table student(sid int primary key auto_increment,name varchar(30) not null,city varchar(20) default 'Pune');
desc student;
insert into student(sid,name) values('0','Harsh'),('0','Veer'),('0','Ramakant'),('0','Sham');
select * from student;

set sql_safe_updates=0;

create table course(cid int,cname varchar(30),fee float,foreign key(cid) references student(sid) on delete cascade on update cascade);
desc course;
insert into course values(1,'Python',37500.5),(2,'Java',42500.5),(3,'CPP',25500.5),(4,'C',17500.5);
select * from course;

select sum(fee) from course;
select avg(fee) from course;
select min(fee) from course;
select max(fee) from course;
select count(fee) from course;

select * from course order by fee;