# 2. DuckDuckGo Search (No API key needed)
from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()

query = "Who is the CEO of Meta?"
results = ddg_search.invoke(query)
print("Results:", results)