# Colleciton type hints
from typing import TypeVar
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Abstraction


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius


class Rectangle(Shape):
    def area(self, length, width):
        return length * width


circle = Circle()
rectangle = Rectangle()

print(circle.area(10))
print(rectangle.area(10, 20))


# Dataclass

@dataclass
class Person:
    name: str
    age: int


person = Person("John", 20)
print(person)


# list
nums: list[int] = [1, 2, 3]
prices: list[float] = [1.2, 3.4, 5.6]
active_users: list[bool] = [True, False, True]
students: list[dict[str, int | str]] = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 21}
]

# tuple
location: tuple[float, float] = (23.100, 29.232)
scores: tuple[int, ...] = (1, 2, 3)

# set
nums: set[int] = {1, 2, 3}
prices: set[float] = {1.2, 3.4, 5.6}
active_users: set[bool] = {True, False}
emails: set[str] = {"jane@gmail.com", "john@gmail.com"}

# dictionary
student: dict[str, str | int | bool | dict | list | tuple] = {
    "name": "John",
    "age": 20,
    "email": "jane@gmail.com",
    "active": True,
    "grades": [1, 2, 3],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "location": (23.100, 29.232),
}

# Function type hints


def list_add(a: list[str], b: list[str]) -> list[str]:
    return a + b


def add(a: int, b: int) -> int:
    return a + b


print(add(1, 10))
print(list_add(["a", "b"], ["c", "d"]))


# None and optional types
student_name = "John"
student_phone: str | None = None

# type alias
type StudentData = dict[str, list[str | int]]

student_data: StudentData = {
    "name": ["John", "Jane"],
    "age": [20, 21]
}


def get_student() -> StudentData:
    return {
        "subjects": ["Math", "Science"],
        "grades": [90, 80]
    }


# Generics
T = TypeVar("T")


def get_value(value: T) -> T:
    return value


print(get_value("hello"))
print(get_value(1))
print(get_value(True))


class Student:
    university = "ABC"

    @classmethod
    def get_university(cls) -> str:
        return cls.university

    @classmethod
    def set_university(cls, university: str) -> None:
        cls.university = university

    @staticmethod
    def is_adult(age: int):
        return age >= 18


print(Student.get_university())

Student.set_university("XYZ")
print(Student.get_university())

print(Student.is_adult(20))

# Exception handling


def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError({
            "success": False,
            "message": "Amount must be greater than 0"
        })

    if amount > balance:
        raise ValueError({
            "success": False,
            "message": "Insufficient balance"
        })

    return balance - amount


try:
    balance = withdraw(1000, 1200)
except ValueError as e:
    print(e.args[0].get("message"))
else:
    print(balance)
finally:
    print("Transaction completed")

# Custom exceptions


class PostNotFoundError(Exception):
    pass


posts = [
    {
        "id": 1,
        "title": "Hello World",
        "content": "This is my first post"
    },
    {
        "id": 2,
        "title": "Hello Python",
        "content": "This is my second post"
    }
]


def get_post(id: int) -> dict:
    for post in posts:
        if post["id"] == id:
            return post

    raise PostNotFoundError("Post not found")


try:
    print(get_post(1))
    print(get_post(2))
    print(get_post(3))
except PostNotFoundError as error:
    print(error)
