mysql –u root –p

Select min(CGPA) from lab_grades;

Select count(*) as total_students, avg(Project_marks) as average_project_marks from lab_grades;

Select sum(Days_Present) from lab_grades;

Select major, min(CGPA) as minCGPA, max(CGPA) as maxCGPA
from lab_grades group by major;

Select major, count(*) from lab_grades group by major;

Select major, min(CGPA) as minCGPA, max(CGPA) as maxCGPA from lab_grades group by major having count(*)>=2;

Select major, min(CGPA) as minCGPA, max(CGPA) as maxCGPA from lab_grades where sub_date<=’2018-09-15’ group by major;

Select Name from lab_grades where Project_marks=(Select max(Project_marks) from lab_grades);

Select Major, Name, Days_present from lab_grades where (Major, Days_present) in (Select Major, min(Days_present) from lab_grades group by Major);

Select * from lab_grades where Major = ‘CSE’ and CGPA>any (Select CGPA from lab_grades where Major = ‘CS’);

Select * from lab_grades where Major = ‘CSE’ and CGPA>all (Select CGPA from lab_grades where Major = ‘CS’);

Select distinct Major from lab_grades L1 where exists (Select * from lab_grades L2 where L2.Major=L1.Major and L2.CGPA<3.7);

Select Name from lab_grades L1 where not exists (Select * from lab_grades L2 where L2.Std_ID!=L1.Std_ID and L2.Project_marks>L1.Project_marks);

Select Name from lab_grades L1 where not exists (Select * from lab_grades L2 where L2.Std_ID!=L1.Std_ID and L2.Project_marks>=L1.Project_marks);

Select Count(*) from lab_grades L1 where not exists (Select * from lab_grades L2 where L2.Std_ID!=L1.Std_ID and L2.Project_marks>L1.Project_marks);

Select Count(*) from lab_grades whereProject_marks = (Select max(Project_marks) from lab_grades);

Select Count(*) from lab_grades where Project_marks > all (Select Project_marks from lab_grades);

Select Major from lab_grades group by Major having Count(*) >= all (Select Count(*) from lab_grades group by Major);

SELECT column_name(s)
FROM table_name(s)
WHERE conditions
GROUP BY column_name(s)
HAVING conditions
ORDER BY column_name(s);