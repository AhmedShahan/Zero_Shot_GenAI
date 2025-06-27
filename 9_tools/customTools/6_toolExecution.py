from langchain_core.tools import tool

@tool
def multiply(a: int, b:int)->int:
    """Multiplication of two integer number"""
    return a*b

from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")

llm_with_tool=llm.bind_tools([multiply])

result=llm_with_tool.invoke("Multiply by 10 with 3")
print("Content: ",result.content)
tool_call=result.tool_calls[0]
print("Tool Calls: ",tool_call)

# result=multiply.invoke(tool_call['args'])
result=multiply.invoke(tool_call)
print(result.content)
