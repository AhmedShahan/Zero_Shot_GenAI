from langchain_core.tools import tool
from langchain_community.tools.arxiv import ArxivQueryRun
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """Multiplication of two integer numbers"""
    return a * b

# Tool setup
from arxive_baseTool import ArxiveSearchTool
arxive_tool = ArxiveSearchTool()
duckduckgo = DuckDuckGoSearchResults()

# LLM setup
llm = ChatCohere(model="command-r-plus")
llm_with_tool = llm.bind_tools([multiply, arxive_tool, duckduckgo])

# Chat history
chat_history = []

# Tool Call Handler
def Tool_Call(tool):
    if tool['name'] == "ArxiveTool":
        result = arxive_tool.invoke(tool)
        content = result.content
        print("Paper Title:", content["Title"])
        chat_history.append(ToolMessage(name="ArxiveTool", content=str(content["Title"])))
    elif tool['name'] == "duckduckgo_results_json":
        result = duckduckgo.invoke(tool)
        print(result.content)
        chat_history.append(ToolMessage(name="duckduckgo_results_json", content=str(result.content)))
    elif tool['name'] == "multiply":
        result = multiply.invoke(tool)
        print(result.content)
        chat_history.append(ToolMessage(name="multiply", content=str(result.content)))

# Prompt template
Message = [
    ('system', 'You are an advanced AI for retriever and answering questions.'),
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

# Chat loop
while True:
    query = input("Enter Query: ")
    if query.lower() in ['exit', 'quit']:
        break

    prompt = ChatPromptTemplate.from_messages(Message)
    formatted_prompt = prompt.format_messages(query=query)

    chat_history.append(HumanMessage(content=query))

    try:
        result = llm_with_tool.invoke(formatted_prompt)
        tool_call = result.tool_calls[0]
        print("Tool Call:", tool_call['name'])
        Tool_Call(tool_call)
    except Exception as e:
        print("No tool used or tool failed, fallback to normal LLM response.")
        result = llm.invoke(query)
        print(result.content)
        chat_history.append(AIMessage(content=result.content))

# Print chat history
print("\n\nChat History")
for item in chat_history:
    print(f"[{item.__class__.__name__}] {item.content}")
