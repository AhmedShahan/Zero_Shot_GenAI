'''
pip install langchain langchain-community polygon-api-client
pip install financial-datasets

'''

import os
from langchain_community.tools.financial_datasets.balance_sheets import BalanceSheets
from langchain_community.tools.financial_datasets.cash_flow_statements import CashFlowStatements
from langchain_community.tools.financial_datasets.income_statements import IncomeStatements
from langchain_community.tools.polygon.aggregates import PolygonAggregates
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.tools.polygon.last_quote import PolygonLastQuote
from langchain_community.tools.polygon.ticker_news import PolygonTickerNews
from  langchain_google_genai  import ChatGoogleGenerativeAI 
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI

# Set up environment variable for Polygon API key (already done if exported)
# os.environ["POLYGON_API_KEY"] = "your_api_key"

# Initialize the LLM (replace with your preferred model)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)
# Initialize each tool
balance_sheets = BalanceSheets()
cash_flow_statements = CashFlowStatements()
income_statements = IncomeStatements()
# polygon_aggregates = PolygonAggregates()
# polygon_financials = PolygonFinancials()
# polygon_last_quote = PolygonLastQuote()
# polygon_ticker_news = PolygonTickerNews()
ticker = "AAPL"
balance_sheet_result = balance_sheets.run(ticker)
print("Balance Sheet for", ticker)
print(balance_sheet_result)
print("\n" + "="*50 + "\n")