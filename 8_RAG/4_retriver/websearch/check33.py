from langchain_community.tools.openweathermap.tool import OpenWeatherMapQueryRun
from langchain_community.utilities.openweathermap import OpenWeatherMapAPIWrapper

# Step 1: Get a valid API key from https://openweathermap.org/api
# Sign up for free and get your API key

# Step 2: Replace with your actual API key
OPENWEATHER_API_KEY = "0f182427f045e4a0ba977faced890dbc"  # Replace this with your real API key

try:
    weather_tool = OpenWeatherMapQueryRun(
        api_wrapper=OpenWeatherMapAPIWrapper(
            openweathermap_api_key=OPENWEATHER_API_KEY,
            # Optional: Specify language (default is 'en')
            # openweathermap_language="en",
        )
    )
    
    # Test the weather query
    result = weather_tool.invoke("What is the weather in New York City?")
    print("Weather Information:", result)
    
except Exception as e:
    print(f"Error occurred: {e}")
    print("\nTroubleshooting steps:")
    print("1. Make sure you have a valid OpenWeatherMap API key")
    print("2. Check that your API key is active (can take a few hours after signup)")
    print("3. Verify you haven't exceeded your API quota")
    print("4. Try a different location format (e.g., 'New York,US' or 'London,UK')")

# Alternative: Test with environment variable
import os

# You can also set the API key as an environment variable
# export OPENWEATHERMAP_API_KEY="your_api_key_here"
# Then use:
"""
weather_tool_env = OpenWeatherMapQueryRun(
    api_wrapper=OpenWeatherMapAPIWrapper(
        openweathermap_api_key=os.getenv("OPENWEATHERMAP_API_KEY")
    )
)
"""

# Example of testing different location formats
def test_weather_locations():
    """Test different location format variations"""
    locations = [
        "New York City",
        "New York,US",
        "NYC",
        "London,UK",
        "Tokyo,JP"
    ]
    
    for location in locations:
        try:
            result = weather_tool.invoke(f"What is the weather in {location}?")
            print(f"✓ {location}: {result}")
        except Exception as e:
            print(f"✗ {location}: Failed - {e}")

# Uncomment to test different locations
test_weather_locations()