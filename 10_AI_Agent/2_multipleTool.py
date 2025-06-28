from langchain_community.tools import PubmedQueryRun, ArxivQueryRun
pubMedSearch=PubmedQueryRun()
# arxivSearch=ArxivQueryRun()
from arxive_baseTool import ArxiveSearchTool
arxivSearch=ArxiveSearchTool()

# print(search_tool.invoke("Recent ai post"))

from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# print(llm.invoke('What is Ai').content)


from langchain import hub
prompt=hub.pull('hwchase17/react')
print(prompt)

from langchain.agents import create_react_agent

agent=create_react_agent(
    llm=llm,
    tools=[pubMedSearch, arxivSearch],
    prompt=prompt
)

from langchain.agents import  AgentExecutor
agent_executor=AgentExecutor(
    agent=agent,
    tools=[pubMedSearch, arxivSearch],
    verbose=True
)

query="Give me Papers of shafin rahman"

result=agent_executor.invoke({
    "input":query
})
print(result)