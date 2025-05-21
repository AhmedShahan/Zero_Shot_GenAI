from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class student(BaseModel):
    name: str = "Ahmed"
    age: int = 20
    ### Lets say আমরা চাচ্ছি cgpa ২-৩  এর মাঝে জাদের তাদের টাই শুধু নিতে তাহলে 
    grade: Optional[float] = Field(ge=2, le=4, default=2.5, description="CGPA should be between 2 and 4")
    is_enrolled: Optional[bool] = None
    email: Optional[EmailStr] = None



## pip install pydantic[email]
new_student3= student(name="Shahan", age=25, grade=3.8, is_enrolled=True, email="abc@gmai.com")
# print(new_student3)

### First convert to dictionary

new_student_dict = dict(new_student3)
print(new_student_dict["name"])


student_json = new_student3.model_dump_json()
