import os
from dotenv import load_dotenv
import pyowm
from langchain_community.tools import TavilySearchResults as TavilySearch
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_classic.prompts import PromptTemplate

load_dotenv()
os.environ["LANGCHAIN_PROJECT"]="ReAct Agent Tracing"

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

arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=3,
    doc_content_chars_max=1000,
    arxiv_search_kwargs={"max_results": 3},
    arxiv_exceptions_on_failure=False  # ← don't crash on errors
)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

tools = [tavily_tool, get_weather, arxiv_tool]

# --- LLM ---
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    model_kwargs={"parallel_tool_calls": False}
)

# --- ReAct Prompt ---
# prompt = PromptTemplate.from_template("""Answer the following questions as best you can. You have access to the following tools:

# {tools}

# Use the following format:

# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [{tool_names}]
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question

# Begin!

# Question: {input}
# Thought:{agent_scratchpad}""")

from langsmith import Client
client = Client()
prompt = client.pull_prompt(
    "llm-react/react",
)
# --- Agent ---
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    handle_tool_errors=True,   # ← add this
    max_iterations=10
)

# --- Run ---
result = agent_executor.invoke({
    "input": "What is the weather in the city where the Attention Is All You Need paper was published and what are the latest news about that paper?"
})
print("\nFinal Answer:", result["output"])