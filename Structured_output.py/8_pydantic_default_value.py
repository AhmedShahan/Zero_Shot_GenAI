from pydantic import BaseModel

class student(BaseModel):
    name: str = "Ahmed"
    age: int = 20
    grade: float = 3.5
    is_enrolled: bool = True

new_student = student()
print(new_student)
print(new_student.name)
print(new_student.age)
print(new_student.grade)
print(new_student.is_enrolled)
print(new_student.__dict__)   ## It will return the full dictionary
print(type(new_student))  ## It will return the type of the object
