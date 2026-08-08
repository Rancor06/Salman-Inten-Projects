-- Create database
CREATE DATABASE portfolio_db;
USE portfolio_db;

-- Create projects table (4 columns)
CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    tech_stack VARCHAR(200)
);

-- Create skills table
CREATE TABLE skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(50),
    proficiency INT CHECK (proficiency BETWEEN 1 AND 100)
);

-- Insert sample project data
INSERT INTO projects (title, description, tech_stack) VALUES
('Academic Certificate Authenticity Validator', 'Smart India Hackathon project: ML-based system to detect forged/manipulated certificates using an OCR and verification pipeline.', 'Python, Machine Learning, OCR'),
('NeuraDocCluster AI', 'Intelligent hierarchical document organization system using TF-IDF and HAC document clustering.', 'R, TF-IDF, HAC'),
('EduTrack', 'Student dropout risk predictor built as capstone for the Innolift Ventures internship.', 'Python, Flask, scikit-learn, React'),
('Generative AI Virtual Try-On', '3D outfit visualization system with image preprocessing, masking, and output optimization.', 'Python, Generative AI, OpenCV');

-- Insert sample skills data
INSERT INTO skills (name, category, proficiency) VALUES
('Python', 'Programming', 80),
('SQL', 'Database', 65),
('C', 'Programming', 70),
('Generative AI / Image Processing', 'AI/ML', 80),
('OCR & Document Verification', 'AI/ML', 75),
('Model Debugging & Optimization', 'AI/ML', 75);

-- Create a dedicated MySQL user for the Flask app
CREATE USER 'portfolio_user'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON portfolio_db.* TO 'portfolio_user'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);