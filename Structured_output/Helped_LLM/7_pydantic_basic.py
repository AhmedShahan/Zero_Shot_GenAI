## Install pydantic
# pip install pydantic

from pydantic import BaseModel


class student(BaseModel):
    name: str
    age: int
    grade: float
    is_enrolled: bool


new_student = student(name="shahan", age=20, grade=3.5, is_enrolled=True)
# print(new_student)
# print(new_student.name)
# print(new_student.age)
# print(new_student.grade)
# print(new_student.is_enrolled)

### This code is working well but if we pass wrong typed data it will throw an error
new_student = student(name="shahan", age="twenty", grade=3.5, is_enrolled=True)
print(new_student)

'''
Traceback (most recent call last):
  File "/home/shahanahmed/Zero_Shot_GenAI/Structured_output.py/7_pydantic_basic.py", line 22, in <module>
    new_student = student(name="shahan", age="twenty", grade=3.5, is_enrolled=True)
  File "/home/shahanahmed/Zero_Shot_GenAI/myvenv/lib/python3.10/site-packages/pydantic/main.py", line 253, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for student
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='twenty', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/int_parsing

'''