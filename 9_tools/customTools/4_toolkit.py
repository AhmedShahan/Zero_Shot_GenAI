from langchain_core.tools import tool

@tool
def addition(a:int, b:int)->int:
    """Addition of two numbers"""
    return a+b


@tool
def multiplication(a:int, b:int)->int:
    """Multiplication of two numbers"""
    return a*b

class MathToolkit:
    def get_tools(self):
        return [addition, multiplication]


toolkit=MathToolkit()
tools=toolkit.get_tools()

for tool in tools:
    print(f"{tool.name} => {tool.description}")