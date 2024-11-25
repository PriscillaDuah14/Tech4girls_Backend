-- Use the database
USE Tech4Girls_DB;


CREATE TABLE IF NOT EXISTS Users(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
--creating courses table
CREATE TABLE IF NOT EXISTS Courses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT UNIQUE ,
    coursename VARCHAR(50) NOT NULL
);
--creating a user_courses table
CREATE TABLE IF NOT EXISTS User_courses(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
    
);

SHOW TABLES;
--inserting samples into the courses
INSERT INTO Courses (coursename)
VALUES ('Mathematcis'),('Int Science'),('Backend development')
mysql> select * from courses;
+----+-----------+---------------------+
| id | course_id | coursename          |
+----+-----------+---------------------+
|  1 |      NULL | Mathematcis         |
|  2 |      NULL | Int Science         |
|  3 |      NULL | Backend development |
|  4 |      NULL | Mathematcis         |
|  5 |      NULL | Int Science         |
|  6 |      NULL | Backend development |
+----+-----------+---------------------+
 
INSERT INTO User_courses (user_id, course_id)
VALUES(1,3),(1,2),(2,1),(2,2),(3,1),(3,2) 
mysql> select * from user_courses;
+---------+-----------+
| user_id | course_id | 
+---------+-----------+  
|       1 |         1 | ---User 1 enrolls in mathematics
|       2 |         1 | ---User 2 enrolls in int science
|       3 |         1 |  --User 3 enrolls in mathematics
+---------+-----------+


SELECT * FROM Courses;
SELECT * FROM User_courses;




