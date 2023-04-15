use oceo;
show tables;
select * from student;

ALTER TABLE student
ADD COLUMN prof_feedback VARCHAR(400) DEFAULT 'No feedback available';

-- alter table student drop column prof_feedback;

desc student;

INSERT INTO student (student_id, email, stud_name, program, dept_name, cpi, pswd, prof_feedback)
VALUES 
('100001', 'student1@example.com', 'John Doe', 'Computer Science', 'Engineering', 3.5, 'password1', 'Good work!'),
('100002', 'student2@example.com', 'Jane Smith', 'Mechanical Engineering', 'Engineering', 3.8, 'password2', 'Keep it up!'),
('100003', 'student3@example.com', 'Bob Johnson', 'Chemistry', 'Science', 3.2, 'password3', 'No feedback available'),
('100004', 'student4@example.com', 'Alice Lee', 'Electrical Engineering', 'Engineering', 3.6, 'password4', 'You can do better.'),
('100005', 'student5@example.com', 'Mark Davis', 'Physics', 'Science', 3.4, 'password5', 'Great job!'),
('100006', 'student6@example.com', 'Karen Brown', 'Biology', 'Science', 3.1, 'password6', 'No feedback available'),
('100007', 'student7@example.com', 'Tom Wilson', 'Civil Engineering', 'Engineering', 3.9, 'password7', 'Keep up the good work!'),
('100008', 'student8@example.com', 'Lisa Garcia', 'Computer Science', 'Engineering', 3.7, 'password8', 'You need to study more.'),
('100009', 'student9@example.com', 'Mike Hernandez', 'Mechanical Engineering', 'Engineering', 3.2, 'password9', 'No feedback available'),
('100010', 'student10@example.com', 'Sarah Johnson', 'Chemistry', 'Science', 3.5, 'password10', 'Good effort!'),
('100011', 'student11@example.com', 'David Lee', 'Electrical Engineering', 'Engineering', 3.4, 'password11', 'No feedback available'),
('100012', 'student12@example.com', 'Emily Davis', 'Physics', 'Science', 3.9, 'password12', 'You are doing well.'),
('100013', 'student13@example.com', 'Ryan Brown', 'Biology', 'Science', 3.1, 'password13', 'No feedback available'),
('100014', 'student14@example.com', 'Anna Wilson', 'Civil Engineering', 'Engineering', 3.8, 'password14', 'You need to work harder.'),
('100015', 'student15@example.com', 'Eric Garcia', 'Computer Science', 'Engineering', 3.6, 'password15', 'Great job!'),
('100016', 'student16@example.com', 'Olivia Hernandez', 'Mechanical Engineering', 'Engineering', 3.3, 'password16', 'No feedback available'),
('100017', 'student17@example.com', 'Jack Johnson', 'Chemistry', 'Science', 3.7, 'password17', 'Keep up the good work!'),
('100018', 'student18@example.com', 'Sophia Lee', 'Electrical Engineering', 'Engineering', 3.2, 'password18', 'No feedback available'),
('100019', 'student19@example.com', 'William Davis', 'Physics', 'Science', 3.4, 'password19', 'Good effort!'),
('100020', 'student20@example.com', 'Micheal Jackson', 'Environmental Science', 'Science', 3.5, 'password20', 'You need to improve your performance.');

select student_id, email, stud_name, program, dept_name, prof_feedback from student;