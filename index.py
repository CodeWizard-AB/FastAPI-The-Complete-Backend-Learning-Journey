# Colleciton type hints
from typing import TypeVar

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
