mysql -u root -p

create database Homework_3;

use Homework_3;

create table Developers ( employee_id char(10), first_name varchar(20), last_name varchar(20), email varchar(60), phone_number char(14), hire_date date, job_id char(10), salary int, commission_pct decimal(5,3), manager_id char(10), department_id char(10));

DESCRIBE Developers;

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP001', 'John', 'Doe', 'johndoe@google.com', '123-456-7890', '2022-01-01', 'JOB001', 5500, 0.05, 'MNG001', 'DPT001');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP002', 'Jane', 'Smith', 'janesmith@google.com', '555-123-4567', '2021-06-15', 'JOB002', 6700, 0.07, 'MNG002', 'DPT002');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP003', 'Tom', 'Jones', 'tomjones@google.com', '222-333-4444', '2022-02-10', 'JOB003', 5500, 0.03, 'MNG003', 'DPT003');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP004', 'Samantha', 'Lee', 'samlee@google.com', '888-555-1234', '2022-01-03', 'JOB001', 65000, 0.06, 'MNG002', 'DPT004');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP005', 'Alex', 'Kim', 'alexkim@google.com', '444-555-6666', '2021-09-20', 'JOB003', 6000, 0.04, 'MNG003', 'DPT005');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP006', 'David', 'Chang', 'davidchang@google.com', '777-888-9999', '2022-01-25', 'JOB002', 2500, 0.02, 'MNG001', 'DPT006');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP007', 'Emily', 'Wong', 'emilywong@google.com', '555-666-7777', '2021-12-01', 'JOB001', 6500, 0.05, 'MNG002', 'DPT004');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP008', 'Jack', 'Liu', 'jackliu@google.com', '111-222-3333', '2021-11-12', 'JOB004', 5000, 0.03, 'MNG001', 'DPT001');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP009', 'Maria', 'Garcia', 'mariagarcia@google.com', '999-888-7777', '2022-02-01', 'JOB003', 6500, 0.06, 'MNG003', 'DPT003');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP010', 'Michael', 'Nguyen', 'michaelnguyen@google.com', '333-444-5555', '2021-10-15', 'JOB004', 7000, 0.08, 'MNG001', 'DPT007');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP011', 'Emily', 'Kim', 'emilykim@amazon.com', '444-555-6666', '2022-02-12', 'JOB002', 9000, 0.05, 'MNG002', 'DPT005');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP012', 'Alex', 'Tran', 'alextran@microsoft.com', '555-666-7777', '2022-01-01', 'JOB003', 35000, 0.04, 'MNG003', 'DPT006');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP013', 'Jennifer', 'Lee', 'jenniferlee@ibm.com', '666-777-8888', '2022-02-01', 'JOB004', 7500, 0.03, 'MNG004', 'DPT004');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP014', 'William', 'Chen', 'williamchen@apple.com', '777-888-9999', '2022-01-15', 'JOB005', 6500, 0.02, 'MNG005', 'DPT002');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP015', 'Andrew', 'Park', 'andrewpark@salesforce.com', '888-999-0000', '2022-02-20', 'JOB002', 2900, 0.06, 'MNG006', 'DPT005');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP016', 'Sophia', 'Garcia', 'sophiagarcia@oracle.com', '999-000-1111', '2022-01-31', 'JOB003', 80000, 0.04, 'MNG007', 'DPT007');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP017', 'Ryan', 'Wang', 'ryanwang@intel.com', '111-222-3333', '2022-02-05', 'JOB004', 7600, 0.03, 'MNG008', 'DPT007');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP018', 'Olivia', 'Davis', 'oliviadavis@facebook.com', '222-333-4444', '2022-02-20', 'JOB001', 35000, 0.01, 'MNG009', 'DPT001');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP019', 'Sarah', 'Lee', 'sarahlee@google.com', '111-222-3333', '2022-01-20', 'JOB005', 6000, 0.07, 'MNG003', 'DPT004');

INSERT INTO Developers (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES ('EMP020', 'David', 'Johnson', 'davidjohnson@google.com', '444-555-6666', '2022-02-01', 'JOB001', 39000, 0.1, 'MNG002', 'DPT003');

Select * From Developers;

SELECT first_name, last_name, email, phone_number, hire_date, department_id FROM Developers WHERE hire_date = (SELECT MAX(hire_date) FROM Developers);

SELECT first_name, last_name, employee_id, phone_number, salary, department_id FROM Developers WHERE (department_id, salary) IN ( SELECT department_id, MIN(salary) FROM Developers GROUP BY department_id ) ORDER BY salary;

SELECT D1.employee_id, D1.first_name, D1.last_name, D1.commission_pct, D1.department_id FROM Developers D1 WHERE D1.department_id = 'DPT007' AND D1.commission_pct < ALL (SELECT D2.commission_pct FROM Developers D2 WHERE D2.department_id = 'DPT005');

SELECT department_id, COUNT(*) AS total_employees FROM Developers WHERE department_id NOT IN ( SELECT DISTINCT department_id FROM Developers WHERE salary > 30000 ) GROUP BY department_id;

SELECT DISTINCT department_id, job_id, commission_pct FROM Developers D1 WHERE commission_pct < ANY ( SELECT commission_pct FROM Developers D2 WHERE D1.department_id = D2.department_id AND D1.job_id <> D2.job_id );

SELECT DISTINCT manager_id FROM Developers WHERE manager_id IS NOT NULL AND manager_id NOT IN ( SELECT DISTINCT manager_id FROM Developers WHERE salary < 3500 );

SELECT D1.first_name, D1.last_name, D1.employee_id, D1.email, D1.salary, D1.department_id, D1.commission_pct FROM Developers D1 WHERE D1.commission_pct = ( SELECT MIN(D2.commission_pct) FROM Developers D2 WHERE D1.manager_id = D2.manager_id );
