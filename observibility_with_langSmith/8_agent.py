from dotenv import load_dotenv
load_dotenv()

## ------------Tools ------------- ##
## Tavily Search Tools
from langchain_community.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults(
    max_results=5,          # Number of results to return
    search_depth="advanced" # "basic" or "advanced"
)

result = search_tool.invoke("What is LangChain?")
print(result)