# # pip install pyowm

import pyowm
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("OPENWEATHER_API_KEY")
owm = pyowm.OWM(api_key=api_key)
mgr = owm.weather_manager()
observation = mgr.weather_at_place("Dhaka,BD")
weather = observation.weather
print(weather.temperature("celsius"))