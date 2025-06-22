# LangChain Tools Python Code Examples

# 1. Bing Search Tool
from langchain_community.tools import BingSearchRun
from langchain_community.utilities import BingSearchAPIWrapper
# Bing Search setup
bing_search = BingSearchAPIWrapper(bing_subscription_key="your_bing_api_key")
bing_tool = BingSearchRun(api_wrapper=bing_search)
result = bing_tool.run("Python tutorial")
print(result)
#***************************************************************************************************************

# 2. DuckDuckGo Search (No API key needed)
from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run("AI news")
print(result)
#***************************************************************************************************************

# 3. Google Search Tool
from langchain_community.tools import GoogleSearchRun
from langchain_community.utilities import GoogleSearchAPIWrapper
google_search = GoogleSearchAPIWrapper(
    google_api_key="your_google_api_key",
    google_cse_id="your_custom_search_engine_id"
)
google_tool = GoogleSearchRun(api_wrapper=google_search)
result = google_tool.run("machine learning")
print(result)
#***************************************************************************************************************

# 4. Wikipedia Search (No API key needed)
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
wikipedia = WikipediaAPIWrapper()
wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)
result = wiki_tool.run("Bangladesh")
print(result)
#***************************************************************************************************************

# 5. File Management Tools (No API key needed)
from langchain_community.tools import ReadFileTool, WriteFileTool
# Read file
read_tool = ReadFileTool()
content = read_tool.run("example.txt")
print(content)
# Write file
write_tool = WriteFileTool()
write_tool.run({
    "file_path": "output.txt", 
    "text": "Hello, this is a test file!"
})
#***************************************************************************************************************

# 6. SQL Database Tool
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_community.utilities import SQLDatabase
# Connect to database
db = SQLDatabase.from_uri("sqlite:///example.db")
sql_tool = QuerySQLDatabaseTool(db=db)
result = sql_tool.run("SELECT * FROM users LIMIT 5")
print(result)
#***************************************************************************************************************

# 7. ArXiv Research Tool (No API key needed)
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
arxiv = ArxivAPIWrapper()
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv)
result = arxiv_tool.run("neural networks")
print(result)
#***************************************************************************************************************

# 8. PubMed Research Tool (No API key needed)
from langchain_community.tools import PubmedQueryRun
from langchain_community.utilities import PubmedAPIWrapper
pubmed = PubmedAPIWrapper()
pubmed_tool = PubmedQueryRun(api_wrapper=pubmed)
result = pubmed_tool.run("covid vaccine")
print(result)
#***************************************************************************************************************

# 9. YouTube Search Tool
from langchain_community.tools import YouTubeSearchTool
youtube_tool = YouTubeSearchTool()
result = youtube_tool.run("Python programming")
print(result)
#***************************************************************************************************************

# 10. Weather Tool
from langchain_community.tools import OpenWeatherMapQueryRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
weather = OpenWeatherMapAPIWrapper(openweathermap_api_key="your_weather_api_key")
weather_tool = OpenWeatherMapQueryRun(api_wrapper=weather)
result = weather_tool.run("Dhaka weather")
print(result)
#***************************************************************************************************************

# 11. Shell Tool (No API key needed)
from langchain_community.tools import ShellTool
shell_tool = ShellTool()
result = shell_tool.run("ls -la")  # Linux/Mac
# result = shell_tool.run("dir")   # Windows
print(result)
#***************************************************************************************************************

# 12. HTTP Requests Tools (No API key needed)
from langchain_community.tools import RequestsGetTool, RequestsPostTool
# GET request
get_tool = RequestsGetTool()
result = get_tool.run("https://api.github.com/users/octocat")
print(result)
# POST request
post_tool = RequestsPostTool()
result = post_tool.run({
    "url": "https://httpbin.org/post",
    "data": {"key": "value"}
})
print(result)
#***************************************************************************************************************

# 13. JSON Tools (No API key needed)
from langchain_community.tools  import JsonGetValueTool
json_tool = JsonGetValueTool()
result = json_tool.run({
    "json_object": {"name": "John", "age": 30},
    "key": "name"
})
print(result)
#***************************************************************************************************************

# 14. Human Input Tool (No API key needed)
from langchain_community.tools import HumanInputRun
human_input_tool = HumanInputRun()
user_input = human_input_tool.run("What's your favorite programming language?")
print(f"User said: {user_input}")
#***************************************************************************************************************

# 15. Wolfram Alpha Tool
from langchain_community.tools import WolframAlphaQueryRun
from langchain_community.utilities import WolframAlphaAPIWrapper
wolfram = WolframAlphaAPIWrapper(wolfram_alpha_appid="your_wolfram_app_id")
wolfram_tool = WolframAlphaQueryRun(api_wrapper=wolfram)
result = wolfram_tool.run("integrate x^2")
print(result)
#***************************************************************************************************************

# 16. Slack Tool
from langchain_community.tools import SlackSendMessage
slack_tool = SlackSendMessage(slack_token="xoxb-your-slack-token")
slack_tool.run({
    "channel": "#general",
    "message": "Hello from LangChain!"
})
#***************************************************************************************************************

# 17. Gmail Tool
from langchain_community.tools import GmailSendMessage
gmail_tool = GmailSendMessage()
gmail_tool.run({
    "to": "recipient@example.com",
    "subject": "Test Email",
    "message": "This is a test email from LangChain!"
})
#***************************************************************************************************************

# 18. Reddit Search Tool (No API key needed)
from langchain_community.tools import RedditSearchRun
from langchain_community.utilities import RedditSearchAPIWrapper
reddit = RedditSearchAPIWrapper()
reddit_tool = RedditSearchRun(api_wrapper=reddit)
result = reddit_tool.run("python programming")
print(result)
#***************************************************************************************************************

# 19. Brave Search Tool
from langchain_community.tools import BraveSearch
brave_tool = BraveSearch(api_key="your_brave_api_key")
result = brave_tool.run("latest AI developments")
print(result)