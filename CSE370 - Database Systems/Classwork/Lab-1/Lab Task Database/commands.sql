mysql -u root -p

show databases;

create database rahadul20101363;

use rahadul20101363;

create table Lab_grades( student_id char(4),name varchar(30),major char(3),section char(1),days_present int,project_marks double,cgpa decimal(3,2),submission_date date );

show tables;

describe lab_grades;

insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s001','Abir','CS','1',10,18.5,3.91,'2018-09-15');


insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s019','Naima','CSE','2',12,20,3.7,'2018-08-14');


insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s002','Nafis','CSE','1',12,20,3.86,'2018-08-15');

insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s003','Tasneem','CS','1',8,18,3.57,'2018-09-18');


insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s004','Nahid','ECE','2',7,16.5,3.25,'2018-08-20');

insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s005','Arafat','CS','2',11,20,4.0,'2018-09-13');

insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s006','Tasneem','CSE','1',12,17.5,3.7,'2018-08-15');

insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s007','Muhtadi','ECE','1',10,19,3.67,'2018-09-16');


insert into lab_grades (student_id,name,major,section,days_present,project_marks,cgpa,submission_date)values ('s008','Farhana','CSE','2',6,15,2.67,'2018-08-16');

select *from lab_grades;