from langchain_core.tools import tool

@tool
def multiply(a:int, b:int)->int:
    """Multiplication of two integer number"""
    return a*b

from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)

## tool binding
llm_with_tool=llm.bind_tools([multiply])

query="Multiply 3 with 5"

result=llm_with_tool.invoke(query)
if result.content:
    print("Without Tool Call Result: ",result)
else:
    result=multiply.invoke(result.tool_calls[0])
    print("With Multiply ToolCall Result:",result.content)
