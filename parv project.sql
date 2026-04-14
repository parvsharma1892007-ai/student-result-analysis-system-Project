CREATE DATABASE parv_project;
USE parv_project;
CREATE TABLE users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(50)
);
CREATE TABLE quiz(
    quiz_id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_title VARCHAR(100)
);
CREATE TABLE questions(
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id INT,
    question TEXT,
    option1 VARCHAR(100),
    option2 VARCHAR(100),
    option3 VARCHAR(100),
    option4 VARCHAR(100),
    correct_answer INT
);
CREATE TABLE results(
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    quiz_id INT,
    score INT
);
INSERT INTO quiz (quiz_title) VALUES
('Computer Basics'),
('DBMS Basics');
INSERT INTO users (name,email,password) VALUES
('Rahul','rahul@gmail.com','123'),
('Aman','aman@gmail.com','123'),
('Priya','priya@gmail.com','123'),
('Riya','riya@gmail.com','123'),
('Karan','karan@gmail.com','123'),
('Neha','neha@gmail.com','123'),
('Simran','simran@gmail.com','123'),
('Arjun','arjun@gmail.com','123'),
('Pooja','pooja@gmail.com','123'),
('Vikas','vikas@gmail.com','123');
INSERT INTO questions 
(quiz_id,question,option1,option2,option3,option4,correct_answer)
VALUES

(1,'What does CPU stand for?',
'Central Process Unit',
'Central Processing Unit',
'Computer Personal Unit',
'Central Processor Unit',
2),

(1,'Which memory is temporary?',
'RAM',
'ROM',
'Hard Disk',
'SSD',
1),

(1,'Which device is input device?',
'Monitor',
'Keyboard',
'Printer',
'Speaker',
2),

(1,'Which language is used for web pages?',
'Python',
'Java',
'HTML',
'C++',
3),

(1,'Which storage is permanent?',
'RAM',
'Cache',
'Hard Disk',
'Register',
3),

(1,'Full form of DBMS?',
'Data Base Management System',
'Digital Base Management System',
'Data Binary Management System',
'None',
1),

(1,'Which key uniquely identifies a record?',
'Primary Key',
'Foreign Key',
'Candidate Key',
'Composite Key',
1),

(1,'Which SQL command retrieves data?',
'SELECT',
'INSERT',
'UPDATE',
'DELETE',
1),

(1,'Which SQL clause filters records?',
'WHERE',
'ORDER BY',
'GROUP BY',
'HAVING',
1),

(1,'Which device processes data?',
'CPU',
'Mouse',
'Keyboard',
'Printer',
1);
INSERT INTO results (user_id,quiz_id,score) VALUES
(1,1,8),
(2,1,7),
(3,1,6),
(4,1,9),
(5,1,5),
(6,1,7),
(7,1,8),
(8,1,6),
(9,1,9),
(10,1,7);
SELECT * FROM users;
SELECT * FROM questions;
SELECT * FROM results;
SELECT AVG(score) AS Average_Score FROM results;
SELECT MAX(score) AS Highest_Score FROM results;
SELECT MIN(score) AS Lowest_Score FROM results;
SELECT user_id, score
FROM results
ORDER BY score DESC;
SELECT COUNT(user_id) AS Total_Students FROM results;
SELECT users.name, results.score
FROM users
JOIN results
ON users.user_id = results.user_id;

