from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, Any, Literal, Annotated
from enum import Enum

app = FastAPI()

students = [
    {
        "name": "jane",
        "age": 10,
        "email": "email@gmail.com",
        "phone": None
    },
    {
        "name": "john",
        "age": 10,
        "email": "email@gmail.com",
        "phone": None
    },
    {
        "name": "python",
        "age": 12,
        "email": "python@gmail.com",
        "phone": None
    }
]


class UserRole(str, Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"


class Student(BaseModel):
    name: str
    age: int
    email: str
    phone: Optional[str] = None
    address: Optional[Any] = None
    status: Literal["active", "inactive"]
    role: UserRole


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}


@app.get('/students')
async def find_students(name: Optional[str] | None = None, age: Optional[int] | None = None, limit: Annotated[int, Query(ge=1, le=100)] = 10):
    find_students = students

    if name:
        find_students = [
            student for student in students if student["name"] == name]

    if age:
        find_students = [
            student for student in students if student["age"] == age]

    return {
        "success": True,
        "data": find_students,
        "limit": limit
    }


@app.post('/students')
async def create_student(student: Student):
    students.append(student)

    return {
        "success": True,
        "message": "Student created successfully",
        "student": student,
    }
