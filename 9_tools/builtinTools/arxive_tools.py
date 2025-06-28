from langchain_community.tools import ArxivQueryRun
tools=ArxivQueryRun()
result=tools.invoke("Give me some paper of Shafin Rahman")
print(result)