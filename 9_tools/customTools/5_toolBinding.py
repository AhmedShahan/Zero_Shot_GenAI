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

print("Tool Calls: ", result.tool_calls[0])
