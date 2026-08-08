CREATE DATABASE IF NOT EXISTS edutrack_db;
USE edutrack_db;

-- Student academic records, managed only by the admin
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(20) UNIQUE NOT NULL,
    attendance_percentage DECIMAL(5,2),
    gpa DECIMAL(3,2),
    dropout_risk VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Login accounts for both the admin and each student
-- student_id is NULL for the admin account, and links to students.id for student accounts
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'student') NOT NULL,
    student_id INT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);
