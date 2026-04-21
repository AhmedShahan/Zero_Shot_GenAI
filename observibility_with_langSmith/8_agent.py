from dotenv import load_dotenv
from langchain_core.tools import tool
import requests
load_dotenv()

## ------------Tools ------------- ##
## Tavily Search Tools

from langchain_tavily import TavilySearch

tool = TavilySearch(
    max_results=3,
    search_depth="advanced",
    include_answer=True,
)

result = tool.invoke("What is Artificial Intelligence?")
print(result)