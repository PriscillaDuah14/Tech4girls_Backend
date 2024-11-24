-- Use the database
USE Tech4Girls_DB;


-- Creating the Posts table with specified columns
CREATE TABLE IF NOT EXISTS Posts (
    user_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,            
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,        
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) 
);

SHOW TABLES;

-- Inserting sample data into the Posts table to create a one-to-many relationship

INSERT INTO Posts (user_id, title, content, created_at) 
VALUES ( 1,'My First Post', 'This is my lifestyle','2024-11-23 10:00:00'),  
( 1,'My Second Post', 'This is my sql assignment content of my second post','2024-11-23 10:00:00'),
( 3,'My daily Post', 'This is the content of my daily life post.','2024-11-23 10:00:00'),      
( 4,'Last Post', 'This is the last post of journal .','2024-11-23 10:00:00');  

SELECT * FROM Posts;

