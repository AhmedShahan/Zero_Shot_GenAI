from pydantic import BaseModel, EmailStr
from typing import Optional
class student(BaseModel):
    name: str
    age: int
    grade: float
    is_enrolled: Optional[bool]
    email: Optional[EmailStr]

## pip install pydantic[email]
new_student3= student(name="Shahan", age=25, grade=3.8,email="abc@gmail.com")
print(new_student3)


'''
Although is_enrolled is optional, it is not required to be present in the input data. Because 
In Pydantic v2, using Optional[bool] without a default value means the field is still required unless explicitly marked as optional with a default like None.
That why we have to set it as None


In a Nutshell, if we provide optional field, then it will requiredd the default value as None or any other value
'''