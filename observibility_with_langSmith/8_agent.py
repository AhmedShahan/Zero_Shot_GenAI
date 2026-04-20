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
def get_weather_data(city: str) -> dict:
    geo = requests.get(
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    ).json()

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    weather = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"  # 👈 add timezone=auto
    ).json()

    return weather

print(get_weather_data("Dhaka"))