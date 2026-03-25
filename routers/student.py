from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ➕ Create Student
@router.post("/")
def add_student(student: schemas.Student, db: Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student added successfully"}


# 📄 Get All Students
@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


# 🔍 Get Student by ID
@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        return student
    return {"error": "Student not found"}


# ✏️ Update Student
@router.put("/{student_id}")
def update_student(student_id: int, updated_student: schemas.Student, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if student:
        student.name = updated_student.name
        student.age = updated_student.age
        student.course = updated_student.course
        db.commit()
        return {"message": "Student updated successfully"}
    
    return {"error": "Student not found"}


# ❌ Delete Student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if student:
        db.delete(student)
        db.commit()
        return {"message": "Student deleted successfully"}
    
    return {"error": "Student not found"}