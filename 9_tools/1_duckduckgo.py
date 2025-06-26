from langchain_community.tools import DuckDuckGoSearchRun
search_tools=DuckDuckGoSearchRun()

result=search_tools.invoke("What is  Ai")
print(result)