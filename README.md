# Email-password-check-and-login-system

User Authentication System (Python Project)

## Overview

This project is a simple command-line User Authentication System implemented in Python. It allows users to register with an email and password, and log in using their credentials. The system validates email format and enforces strong password rules.

## Features

User registration
User login
Email format validation using regex
Strong password validation
Simple and interactive command-line interface

## Technologies Used

Python
Regular Expressions (re module)
Dictionary data structure

## How to Run

install python (VS Code)
Run the program: user authentication system.py

## How It Works

User enters email during registration
The system validates email using regex pattern
Password must satisfy the following conditions:
Minimum 8 characters
At least one digit
At least one uppercase letter
At least one lowercase letter
At least one special character (@#$%&*!-)

If valid, user is stored in a dictionary as:
email,password

During login, entered credentials are matched with stored data

## Future Improvements

Store user data in file or database
Encrypt passwords for security
Add password reset feature
Implement multi-user session handling
Convert to web application using Flask

## Author
Harsha G
Learning Python | Embedded Systems | IoT
