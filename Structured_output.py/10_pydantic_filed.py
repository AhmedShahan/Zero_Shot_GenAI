from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class student(BaseModel):
    name: str = "Ahmed"
    age: int = 20
    ### Lets say আমরা চাচ্ছি cgpa ২-৩  এর মাঝে জাদের তাদের টাই শুধু নিতে তাহলে 
    grade: Optional[float] = Field(ge=2, le=4, default=2.5)
    is_enrolled: Optional[bool] = None
    email: Optional[EmailStr] = None



## pip install pydantic[email]
new_student3= student(name="Shahan", age=25, grade=3.8, is_enrolled=True, email="abc@gmai.com")
print(new_student3)

############# This will works but let say cgpa=1.5 then it will throw an error
new_student4= student(name="Shahan", age=25, grade=1.5, is_enrolled=True)
'''
  Input should be greater than or equal to 2 [type=greater_than_equal, input_value=1.5, input_type=float]
    For further information visit https://errors.pydantic.dev/2.11/v/greater_than_equal
'''