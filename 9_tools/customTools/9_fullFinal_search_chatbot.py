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


@tool
def ArxiveTool(query: str, k: int, full_document: bool = False, load_all_meta: bool = False) -> list:
    """Fetch Document from Arxiv using Arxiv Retriever"""
    from langchain.retrievers import ArxivRetriever

    retriever = ArxivRetriever(
        top_k_results=k,
        get_full_documents=full_document,
        load_all_available_meta=load_all_meta,
    )
    docs = retriever.invoke(query)
    return docs


arxive_tool = ArxivRetriever()
duckduckgo=DuckDuckGoSearchResults()

from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
# llm = ChatCohere(model="command-r-plus")

## tool binding
llm_with_tool=llm.bind_tools([multiply,arxive_tool,duckduckgo])

def Tool_Call(tool):
    if tool['name'] == "arxiv":
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
