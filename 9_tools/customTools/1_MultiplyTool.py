from langchain_core.tools import tool
@tool
def multiply(num1:int, num2:int)-> int:
    """Multiply two  numbers"""
    return num1  * num2

result=multiply.invoke({"num1":5, "num2":10})
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

print(multiply.args_schema.model_json_schema()) 