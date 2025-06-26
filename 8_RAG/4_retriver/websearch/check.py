# from langchain_community.tools import RedditSearchRun
# # 1. Reddit Search (No API key needed)
# reddit_search = RedditSearchRun()
# query = "Who is the CEO of Meta?"
# results = reddit_search.invoke(query)
# print("Results:", results)

'''
pip install pyowm
'''

from langchain_community.tools.openweathermap.tool import OpenWeatherMapQueryRun
from langchain_community.utilities.openweathermap import OpenWeatherMapAPIWrapper

weather_tool = OpenWeatherMapQueryRun(
    api_wrapper=OpenWeatherMapAPIWrapper(
        openweathermap_api_key="0f182427f045e4a0ba977faced890dbc",  # Demo API key
        # openweathermap_base_url="http://api.openweathermap.org/data/2.5/",
        # openweathermap_language="en",
    )
)

result = weather_tool.invoke("What is the weather in New York, US City?")
print("Weather Information:", result)