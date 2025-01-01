Alter table lab_grades add Project_title char(10);

Alter table lab_grades modify column Project_title varchar(50);

Alter table lab_grades drop column Project_title;

Update lab_grades set Major = 'CSE' where name= 'Arafat';

Update lab_grades set Name='Naheed', Project_marks =16 where student_id = 's004';

Delete from lab_grades where Name= 'Naima';

Delete from lab_grades where Days_present < 8 ;

Drop table lab_grades;

Drop database rahadul20101363;



Select student_id, name, project_marks from lab_grades;

Select name, project_marks+days_present*5/12 as total_marks from lab_grades;

Select Upper(Name), Lower(Name) from lab_grades;

Select major from lab_grades;

Select distinct major from lab_grades;

Select * from lab_grades order by name;

Select * from lab_grades order by name desc, submission_date asc;

Select name,project_marks from lab_grades where major='CSE' ;

Select name,project_marks from lab_grades where project_marks between 17 and 19 ;

Select * from lab_grades where major in ('CSE', 'CS');

Select * from lab_grades where project_marks>18 and submission_date between '2018-08-01' and '2018-08-31';

Select * from lab_grades where name like 'a%';

Select * from Lab_Grades where Name like ‘%a%a%’;

Select * from Lab_Grades where Name like 'a___';