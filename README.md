# Student Management REST API (FastAPI)

## Project Overview
This is a Student Management REST API built using FastAPI.  
It supports full CRUD operations with database integration using SQLAlchemy and SQLite.

---

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## Features
-  Create Student
-  Get All Students
-  Get Student by ID
-  Update Student
-  Delete Student
-  Data validation using Pydantic
-  Modular project structure

---

## Project Structure
student-api/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│ ├── init.py
│ └── student.py
├── requirements.txt
└── students.db

---

## Run Project

```bash
uvicorn main:app --reload

API Documentation

Swagger UI:
http://127.0.0.1:8000/docs

```
## Key Highlights

Designed RESTful APIs using FastAPI
Implemented database operations using SQLAlchemy ORM
Used Pydantic for request validation
Followed modular backend architecture

## Author
Om Masal
