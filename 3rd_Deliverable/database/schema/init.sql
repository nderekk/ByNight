-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS bynight;
USE bynight;

-- Users table
drop table if exists users;
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role ENUM('customer', 'manager', 'staff') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert dummy users
-- Note: These passwords are hashed versions of 'password123'
-- In a real application, you would use bcrypt or similar to hash passwords
INSERT INTO users (username, email, password_hash, first_name, last_name, role) VALUES
('john_doe', 'john@example.com', '$2b$10$YourHashedPasswordHere1', 'John', 'Doe', 'user'),
('jane_smith', 'jane@example.com', '$2b$10$YourHashedPasswordHere2', 'Jane', 'Smith', 'user'),
('admin_user', 'admin@bynight.com', '$2b$10$YourHashedPasswordHere3', 'Poutsos', 'Kavlomenos', 'user'),
('venue_owner1', 'owner@venue.com', '$2b$10$YourHashedPasswordHere4', 'Alice', 'Owens', 'manager');

CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email); 

select * from users;