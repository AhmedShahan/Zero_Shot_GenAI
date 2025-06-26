# Web-based Tools যেগুলো Internet থেকে তথ্য আনে

# ===== SEARCH ENGINES =====
from langchain_community.tools.bing_search.tool import BingSearchResults, BingSearchRun
from langchain_community.tools.brave_search.tool import BraveSearch  
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults, DuckDuckGoSearchRun
from langchain_community.tools.google_search.tool import GoogleSearchResults, GoogleSearchRun
from langchain_community.tools.google_serper.tool import GoogleSerperResults, GoogleSerperRun
from langchain_community.tools.jina_search.tool import JinaSearch
from langchain_community.tools.metaphor_search import MetaphorSearchResults
from langchain_community.tools.mojeek_search.tool import MojeekSearch
from langchain_community.tools.searchapi.tool import SearchAPIResults, SearchAPIRun
from langchain_community.tools.searx_search.tool import SearxSearchResults, SearxSearchRun
from langchain_community.tools.tavily_search import TavilyAnswer, TavilySearchResults
from langchain_community.tools.you.tool import YouSearchTool

# ===== ACADEMIC & RESEARCH =====
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.tools.pubmed.tool import PubmedQueryRun  
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.tools.google_books import GoogleBooksQueryRun
from langchain_community.tools.stackexchange.tool import StackExchangeTool

# ===== NEWS & MEDIA =====
from langchain_community.tools.asknews.tool import AskNewsSearch
from langchain_community.tools.reddit_search.tool import RedditSearchRun
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.tools.youtube.search import YouTubeSearchTool

# ===== FINANCIAL DATA =====
from langchain_community.tools.financial_datasets.balance_sheets import BalanceSheets
from langchain_community.tools.financial_datasets.cash_flow_statements import CashFlowStatements
from langchain_community.tools.financial_datasets.income_statements import IncomeStatements
from langchain_community.tools.polygon.aggregates import PolygonAggregates
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.tools.polygon.last_quote import PolygonLastQuote
from langchain_community.tools.polygon.ticker_news import PolygonTickerNews

# ===== SPECIALIZED SERVICES =====
from langchain_community.tools.openweathermap.tool import OpenWeatherMapQueryRun
from langchain_community.tools.merriam_webster.tool import MerriamWebsterQueryRun
from langchain_community.tools.nasa.tool import NasaAction
from langchain_community.tools.steam.tool import SteamWebAPIQueryRun
from langchain_community.tools.google_places.tool import GooglePlacesTool
from langchain_community.tools.wolfram_alpha.tool import WolframAlphaQueryRun

# ===== WEB REQUESTS =====
from langchain_community.tools.requests.tool import (
    RequestsGetTool, RequestsPostTool, RequestsPutTool, 
    RequestsDeleteTool, RequestsPatchTool
)

# Usage Examples:

# 1. DuckDuckGo Search (No API key needed)
ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run("artificial intelligence news")

# 2. Wikipedia Search  
wiki_search = WikipediaQueryRun()
result = wiki_search.run("machine learning")

# 3. ArXiv Research Papers
arxiv_search = ArxivQueryRun()
result = arxiv_search.run("deep learning transformers")

# 4. PubMed Medical Research
pubmed_search = PubmedQueryRun() 
result = pubmed_search.run("covid-19 treatment")

# 5. Tavily Search (with API key)
tavily_search = TavilySearchResults(api_key="your_api_key")
result = tavily_search.run("latest technology trends")

# 6. Google Search (with API key)
google_search = GoogleSearchRun(
    api_wrapper=GoogleSearchAPIWrapper(
        google_api_key="your_api_key",
        google_cse_id="your_cse_id"
    )
)

# 7. Bing Search (with API key)
bing_search = BingSearchRun(api_wrapper=BingSearchAPIWrapper(
    bing_subscription_key="your_bing_key"
))

# 8. YouTube Search
youtube_search = YouTubeSearchTool()
result = youtube_search.run("python programming tutorial")

# 9. Reddit Search  
reddit_search = RedditSearchRun()
result = reddit_search.run("programming tips")

# 10. Weather Information
weather_tool = OpenWeatherMapQueryRun(
    api_wrapper=OpenWeatherMapAPIWrapper(
        openweathermap_api_key="your_weather_api_key"
    )
)

# 11. Financial News
finance_news = YahooFinanceNewsTool()
result = finance_news.run("AAPL")

# 12. Stack Exchange
stack_exchange = StackExchangeTool()
result = stack_exchange.run("python error handling")

# 13. Ask News (Latest News)
ask_news = AskNewsSearch(api_key="your_asknews_api_key")
result = ask_news.run("breaking news today")

# 14. Wolfram Alpha
wolfram = WolframAlphaQueryRun(
    api_wrapper=WolframAlphaAPIWrapper(
        wolfram_alpha_appid="your_wolfram_id"
    )
)

# 15. Web Requests
get_tool = RequestsGetTool()
result = get_tool.run("https://api.example.com/data")