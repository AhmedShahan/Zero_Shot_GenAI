from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

## create the function with type hints
def multiply_function(num1:int, num2: int)->int:
    return num1* num2

## Creating Pydantic Basemodel class

class  MultiplyInput(BaseModel):
    num1: int = Field(required=True, description="This is the First Input to multiply")
    num2: int = Field(required=True, description="This is the Second Input to multiply")

structured_tool=StructuredTool(
    name="multiply",
    description="Multiply two number",
    func=multiply_function,
    args_schema=MultiplyInput
)
result=structured_tool.invoke({
    "num1":10,
    "num2":20
    })
print(result)