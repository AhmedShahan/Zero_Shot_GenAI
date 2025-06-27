from langchain_core.tools import tool
from langchain_community.tools.arxiv import ArxivQueryRun
from langchain_community.tools import DuckDuckGoSearchResults
@tool
def multiply(a:int, b:int)->int:
    """Multiplication of two integer number"""
    return a*b

tavily_tool = ArxivQueryRun()
duckduckgo=DuckDuckGoSearchResults()

from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)

## tool binding
llm_with_tool=llm.bind_tools([multiply,tavily_tool,duckduckgo])

query="Conference paper on sign language"
result=llm_with_tool.invoke(query)
tool_call=result.tool_calls[0]
print("Tool Calls: ",tool_call)

# result=llm_with_tool.invoke(query)
# if result.content:
#     print("Without Tool Call Result: ",result)
# else:
#     result=multiply.invoke(result.tool_calls[0])
#     print("With Multiply ToolCall Result:",result.content)
