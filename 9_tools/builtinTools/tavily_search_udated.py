
from dotenv import load_dotenv
load_dotenv()
from langchain_tavily import TavilySearch

tool = TavilySearch(
    max_results=3,
    topic="news",
    search_depth="advanced",
    include_answer=True,
    include_raw_content=False,
    include_images=True,
    include_image_descriptions=True,
    time_range="week",
    include_domains=["bbc.com"],
    exclude_domains=["pinterest.com"],
    country="bangladesh",
    include_favicon=False,
    include_usage=True
)

result = tool.invoke("What is Artificial Intelligence?")
print(result)