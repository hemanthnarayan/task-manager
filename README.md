# Task Manager with User Authentication

A Python-based console application that allows users to securely manage their tasks using a login and registration system.

---

# 📌 Project Overview

This project is a menu-driven Task Manager application developed using Python. The application supports user authentication and allows each user to manage their own tasks separately.

Users can:
- Register with a username and password
- Login securely
- Add tasks
- View tasks
- Mark tasks as completed
- Delete tasks
- Logout safely

The project also uses file handling with JSON files to store user credentials and tasks persistently.

---

# 🚀 Features

## User Authentication
- User Registration
- Secure Login System
- Password Hashing using SHA-256

## Task Management
- Add Tasks
- View Tasks
- Mark Tasks as Completed
- Delete Tasks

## File Handling
- Persistent storage using JSON files
- Separate storage for users and tasks

## Exception Handling
- Prevents crashes from invalid input
- Handles file and JSON errors safely

---

# 🛠 Technologies Used

- Python 3
- JSON File Handling
- hashlib
- os module

---

# 📂 Project Structure

```text
task-manager/
│
├── task_manager.py
├── users.json
├── tasks.json
├── README.md
