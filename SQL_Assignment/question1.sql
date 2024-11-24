-- Create the database
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;
SHOW DATABASES;


-- Use the database
USE Tech4Girls_DB;

-- Create the Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;

-- Insert sample data into the Users table
INSERT INTO Users (username, email, created_at) 
VALUES ('Priscilla', 'prissy55@gmail.com', '2024-11-01 10:30:00'),
('Emefa', 'emefa66@gmail.com', '2024-11-02 12:00:00'),
('Adjoa', 'adjoa444@gmail.com', '2024-11-03 14:15:00');


--DELETE FROM Users WHERE email = 
SELECT * FROM Users;