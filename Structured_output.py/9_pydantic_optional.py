from pydantic import BaseModel, EmailStr
from typing import Optional
class student(BaseModel):
    name: str = "Ahmed"
    age: int = 20
    grade: float = 3.5
    is_enrolled: Optional[bool] = None
    email: Optional[EmailStr] = None

new_student = student()
print(new_student)
print(new_student.name)
print(new_student.age)
print(new_student.grade)
print(new_student.is_enrolled)
print(new_student.__dict__)   ## It will return the full dictionary
print(type(new_student))  ## It will return the type of the object



new_student1= student(name="Ali", age=25, grade=3.8, is_enrolled=True)
print(new_student1)


## pip install pydantic[email]
new_student3= student(name="Shahan", age=25, grade=3.8, is_enrolled=True, email="abc")
print(new_student3)