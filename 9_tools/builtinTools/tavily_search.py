from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv
load_dotenv()


# Tool তৈরি করো
search_tool = TavilySearchResults(
    max_results=3,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=False,
    include_images=False,
    include_domains=["github.com", "docs.python.org"],
    exclude_domains=["pinterest.com"]
)

# Search চালাও
result = search_tool.invoke("What is LangChain?")

print(result)
