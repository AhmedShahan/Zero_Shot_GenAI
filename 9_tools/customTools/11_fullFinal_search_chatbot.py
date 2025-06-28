from langchain_core.tools import tool
from langchain_community.tools.arxiv import ArxivQueryRun
from langchain.retrievers import ArxivRetriever
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
load_dotenv()
@tool
def multiply(a:int, b:int)->int:
    """Multiplication of two integer number"""
    return a*b



from arxive_baseTool import ArxiveSearchTool
arxive_tool = ArxiveSearchTool()
duckduckgo=DuckDuckGoSearchResults()

from langchain_google_genai import ChatGoogleGenerativeAI
# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
llm = ChatCohere(model="command-r-plus")

## tool binding
llm_with_tool=llm.bind_tools([multiply,arxive_tool,duckduckgo])

def Tool_Call(tool):
    if tool['name'] == "ArxiveTool":
        result=arxive_tool.invoke(tool)
        content=result.content
        print("Paper Title: ",content["Title"])


while True:
    query=input("enter Query: ")
    result=llm_with_tool.invoke(query)
    try:
        tool_call=result.tool_calls[0]
        print("Tool Calls: ",tool_call['name'])
        Tool_Call(tool_call)

    except:
        result=llm.invoke(query)
        print(result.content)
'''
In this code there some problem. Like
If i say Give me some paper about sign language, there some time it misleading and try to answer using llm or duckduck go. 

Although arxiv is specifically for conference paper so we can specifically we can mention somee keyword to use arxiv directly 
as like papers, authors, abstract, conference paper, doi etc
So the solution is to use "Message"
'''