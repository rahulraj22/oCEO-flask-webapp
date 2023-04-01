use oceo;
show tables;
desc oceo_positions;
alter table oceo_positions modify column duration varchar(100);

INSERT INTO oceo_positions (job_id, emp_name, emp_id, act, job_desc, prereq, eligi, total_job, duration, app_status)
VALUES
  (1, 'John Smith', 1001, 'Sales', 'Sales Manager', 'Bachelor''s degree', '5+ years sales', 3, '12 months', 'Open'),
  (2, 'Sarah Johnson', 1002, 'IT', 'Web Developer', 'Bachelor''s degree', '2+ years exp', 2, '18 months', 'Open'),
  (3, 'David Lee', 1003, 'HR', 'HR Manager', 'Master''s degree', '5+ years HR exp', 1, '24 months', 'Closed'),
  (4, 'Karen Brown', 1004, 'Finance', 'Finance Analyst', 'Bachelor''s degree', '2+ years finance', 4, '6 months', 'Open'),
  (5, 'Michael Chen', 1005, 'Sales', 'Sales Representative', 'High school diploma', '1+ years sales', 10, '3 months', 'Open'),
  (6, 'Emily Wilson', 1006, 'Marketing', 'Marketing Specialist', 'Bachelor''s degree', '3+ years marketing', 2, '12 months', 'Open'),
  (7, 'Daniel Kim', 1007, 'IT', 'IT Support Technician', 'Associate''s degree', '1+ years IT', 5, '6 months', 'Open'),
  (8, 'Jessica Park', 1008, 'HR', 'Recruiter', 'Bachelor''s degree', '2+ years HR exp', 3, '9 months', 'Open'),
  (9, 'Matthew Lee', 1009, 'Finance', 'Financial Manager', 'Master''s degree', '5+ years finance', 1, '24 months', 'Closed'),
  (10, 'Amanda Brown', 1010, 'Sales', 'Sales Manager', 'Bachelor''s degree', '5+ years sales', 2, '12 months', 'Open'),
  (11, 'Steven Kim', 1011, 'IT', 'Software Engineer', 'Bachelor''s degree', '3+ years software', 2, '18 months', 'Open'),
  (12, 'Lisa Lee', 1012, 'HR', 'HR Generalist', 'Bachelor''s degree', '2+ years HR exp', 4, '6 months', 'Open'),
  (13, 'Peter Chen', 1013, 'Finance', 'Financial Analyst', 'Bachelor''s degree', '1+ years finance', 5, '3 months', 'Open'),
  (14, 'Jennifer Lee', 1014, 'Marketing', 'Marketing Manager', 'Master''s degree', '5+ years marketing', 1, '24 months', 'Closed'),
  (15, 'Kevin Kim', 1015, 'IT', 'IT Manager', 'Bachelor''s degree', '5+ years IT', 1, '24 months', 'Closed'),
  (16, 'Olivia Park', 1016, 'HR', 'Benefits Specialist', 'Bachelor''s degree', '2+ years HR exp', 3, '9 months', 'Open'),
  (17, 'Thomas Lee', 1017, 'Finance', 'Accountant', 'Bachelor''s degree', '2+ years accounting', 3, '6 months', 'Open'),
  (18, 'Maggie Brown', 1018, 'Sales', 'Sales Associate', 'High school diploma', 'No experience required', 15, '3 months', 'Open'),
(19, 'Jacob Lee', 1019, 'IT', 'Database Administrator', 'Bachelor''s degree', '3+ years database', 2, '18 months', 'Open'),
(20, 'Rachel Kim', 1020, 'Marketing', 'Marketing Coordinator', 'Bachelor''s degree', '1+ years marketing', 4, '6 months', 'Open');

select * from oceo_positions;
