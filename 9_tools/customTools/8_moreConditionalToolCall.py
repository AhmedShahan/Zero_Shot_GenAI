from langchain_core.tools import tool
from langchain_community.tools.arxiv import ArxivQueryRun
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
load_dotenv()
@tool
def multiply(a:int, b:int)->int:
    """Multiplication of two integer number"""
    return a*b

tavily_tool = ArxivQueryRun()
duckduckgo=DuckDuckGoSearchResults()

from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
# llm = ChatCohere(model="command-r-plus")

## tool binding
llm_with_tool=llm.bind_tools([multiply,tavily_tool,duckduckgo])

while True:
    query=input("enter Query: ")
    result=llm_with_tool.invoke(query)
    # print(result.content)
    try:
        tool_call=result.tool_calls[0]
        print("Tool Calls: ",tool_call['name'])
    except:
        result=llm.invoke(query)
        print(result.content)
