## Install pydantic
# pip install pydantic

from pydantic import BaseModel


class student(BaseModel):
    name: str
    age: int
    grade: float
    is_enrolled: bool


new_student = student(name="shahan", age=20, grade=3.5, is_enrolled=True)
print(new_student)
print(new_student.name)
print(new_student.age)
print(new_student.grade)
print(new_student.is_enrolled)
