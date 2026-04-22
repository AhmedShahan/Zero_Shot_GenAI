from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langsmith import Client
import pyowm
import os

load_dotenv()

# --- Tools ---
tavily_tool = TavilySearch(max_results=3, search_depth="advanced", include_answer=True)

@tool
def get_weather(city: str) -> str:
    """Get the current temperature and feels like temperature for a given city.
    Input should be in 'City,CountryCode' format e.g. 'Dhaka,BD'"""
    owm = pyowm.OWM(os.getenv("OPENWEATHER_API_KEY"))
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temp = weather.temperature("celsius")
    return f"Temperature: {temp['temp']}°C, Feels like: {temp['feels_like']}°C"

# ✅ Fixed: limit max_results to avoid 429
arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=3,
    doc_content_chars_max=1000,
    arxiv_search_kwargs={"max_results": 3}
)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

tools = [tavily_tool, get_weather, arxiv_tool]

# --- LLM ---
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,  # use 0 for tool calling, not 0.2
    model_kwargs={"parallel_tool_calls": False}  # ✅ fixes malformed JSON
)

# --- Prompt & Agent ---
client = Client()
prompt = client.pull_prompt("react-agent-executor/react-agent-executor")

agent_executor = create_react_agent(llm, tools)

result = agent_executor.invoke({
    "messages": [("human", "Current Temperature of leaving Shahan Ahmed from North South University")]
})
print(result["messages"][-1].content)