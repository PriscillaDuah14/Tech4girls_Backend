-- Use the database
USE Tech4Girls_DB;

CREATE TABLE IF NOT EXISTS Users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Posts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) 
);

SHOW TABLES;

INSERT INTO Posts (user_id, title, content) 
VALUES
(1, 'My First Post', 'This is the content of the first post.'),
(1, 'Another Post', 'Here is another post from user 1.'),
(2, 'A Post by User 2', 'Content of user  post.'),
(3, 'User 3 Post', 'User 3 has posted this content.');

SELECT * FROM Posts;
--OUTPUT
+----+---------+------------------+----------------------------------------+---------------------+
| id | user_id | title            | content                                | created_at          |
+----+---------+------------------+----------------------------------------+---------------------+
|  1 |       1 | My First Post    | This is the content of the first post. | 2024-11-24 16:50:19 |
|  2 |       1 | Another Post     | Here is another post from user 1.      | 2024-11-24 16:50:19 |
|  3 |       2 | A Post by User 2 | Content of user  post.                 | 2024-11-24 16:50:19 |
|  4 |       3 | User 3 Post      | User 3 has posted this content.        | 2024-11-24 16:50:19 |
+----+---------+------------------+----------------------------------------+---------------------+


