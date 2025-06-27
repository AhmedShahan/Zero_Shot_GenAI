from langchain_core.tools import  BaseTool
from pydantic import BaseModel, Field
from typing import Type
class MultiplyInput(BaseModel):
    a: int =  Field(required=True, description="The first input to Multiply")
    b: int =  Field(required=True, description="The second input to Multiply")

class MultiplyTool(BaseTool):
    name: str =  "multiply"
    description: str= "Multiply two numers"
    args_schema: Type[BaseModel]=MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

tool=MultiplyTool()
result=tool.invoke({
    "a":10,
    "b":20
})
print(result)
print(tool.name)
print(tool.description)
print(tool.args_schema)
