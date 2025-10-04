create database h3;
use h3;
set sql_safe_updates=0;

create table student(sid int,sname varchar(30));
insert into student values(1,"Harsh"),(2,"Veer"),(3,"Raj"),(4,"Ramakant"),(5,"Sushil"); 
select * from student;

create table book(bid int,bname varchar(20),bprice float);
insert into book values(1,"Python",950.5),(2,"Java",855),(3,"C",900.8),(4,"CPP",750),(5,"HTML",900),(2,"CSS",450),(4,"JS",999.9),(1,"Mock Test",200);
select * from book;

select * from book order by bprice desc;
select bprice,count(bid) from book group by bprice;
select bprice,count(bid) from book group by bprice having bprice>500;
select * from book limit 4;
select distinct bid from book;

select s.sid,s.sname,b.bname,b.bprice from student s left join book b on s.sid=b.bid;
select s.sid,s.sname,b.bname,b.bprice from student s right join book b on s.sid=b.bid;
select s.sid,s.sname,b.bname,b.bprice from student s inner join book b on s.sid=b.bid;
select * from student s right join book b on s.sid=b.bid union select * from student s left join book b on s.sid=b.bid;