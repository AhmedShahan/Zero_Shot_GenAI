# # # pip install pyowm

# import pyowm
# from dotenv import load_dotenv
# load_dotenv()
# import os
# api_key=os.getenv("OPENWEATHER_API_KEY")
# owm = pyowm.OWM(api_key=api_key)
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place("Dhaka,BD")
# weather = observation.weather
# print(weather.temperature("celsius"))


# pip install pyowm langchain langchain-core python-dotenv

import pyowm
import os
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Get the current temperature and feels like temperature for a given city. Input should be in 'City,CountryCode' format e.g. 'Dhaka,BD'"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    owm = pyowm.OWM(api_key=api_key)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temp = weather.temperature("celsius")
    return f"Temperature: {temp['temp']}°C, Feels like: {temp['feels_like']}°C"