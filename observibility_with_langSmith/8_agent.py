from dotenv import load_dotenv
from langchain_core.tools import tool
import requests
load_dotenv()

## ------------Tools ------------- ##
## Tavily Search Tools
# from langchain_community.tools.tavily_search import TavilySearchResults

# search_tool = TavilySearchResults(
#     max_results=5,          # Number of results to return
#     search_depth="advanced" # "basic" or "advanced"
# )

# result = search_tool.invoke("What is LangChain?")
# print(result)

import os
### Weather API
# def get_weather_data(city: str) -> dict:
#     geo = requests.get(
#         f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
#     ).json()

#     lat = geo["results"][0]["latitude"]
#     lon = geo["results"][0]["longitude"]

#     weather = requests.get(
#         f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"  # 👈 add timezone=auto
#     ).json()

#     return weather

# print(get_weather_data("Dhaka"))



@tool
def ArxiveTool(query: str, k: int, full_document: bool = False, load_all_meta: bool = False) -> list:
    """Fetch Document from Arxiv using Arxiv Retriever"""
    from langchain_community.retrievers import ArxivRetriever

    retriever = ArxivRetriever(
        top_k_results=k,
        get_full_documents=full_document,
        load_all_available_meta=load_all_meta,
    )
    docs = retriever.invoke(query)
    return docs


query = "au:Shafin_Rahman"  # 👈 this is the fix
results=ArxiveTool.invoke({
    "query": query,
    "k":3
})
print(results)