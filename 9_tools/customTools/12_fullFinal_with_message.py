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


Message=[
    ('system','You are and Advance AI for retriever and answer the questions.'),
    ('human', """
The user has asked: "{query}"

You have access to three tools:
1. ArxivTool — for academic research, conference papers, author-based searches, DOIs, or abstracts.
2. DuckDuckGo — for general web information, non-academic searches, news, or anything broader.
3. multiply — for basic math tasks.

Use ArxivTool **only if** the query is explicitly about research papers, academic topics, DOIs, or publications.
Otherwise, prefer DuckDuckGo or answer using your own knowledge.
""")

]
from langchain.prompts import ChatPromptTemplate
while True:
    query=input("enter Query: ")
    prompt=ChatPromptTemplate.from_messages(Message)
    formatted_prompt = prompt.format_messages(query=query)
    result=llm_with_tool.invoke(formatted_prompt)
    try:
        tool_call=result.tool_calls[0]
        print("Tool Calls: ",tool_call['name'])
        Tool_Call(tool_call)

    except:
        result=llm.invoke(query)
        print(result.content)
