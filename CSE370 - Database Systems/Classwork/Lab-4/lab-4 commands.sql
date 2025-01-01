Select Name, Role From Employee Where Name Like 'a%' Or Where Name Like '%e';

Select * From Employee Where Salary Between 40000 And 60000;

Select * From Employee Where Year(Joining_Date) < 2000;

Update Employee Set Salary = Salary * 1.05 Where role = 'Sales Executive'; 
Select Name, Role, Salary from Employee where Role = 'Sales Executive';

Select Salary * 0.2 AS Michel_Bonus From Employee Where Name = "Michael Scott";

Select * From Employee Order By Salary DESC;

Select * From Employee Order By Age ASC;

Select * From Employee Where Age > 35 And Joining_Date < '2003-01-01';

Delete From Employee Where Name = 'Creed Bratton';

Select * From Employee Where Role Like '%Executive%';

Alter Table Employee CHANGE Name Employee_Name VARCHAR(255);

Alter Table Employee ADD Bonus DECIMAL(10,2);

Alter Table Employee Drop Column Bonus;

Select Distinct Role From Employee;