# from langchain_community.tools import RedditSearchRun
# # 1. Reddit Search (No API key needed)
# reddit_search = RedditSearchRun()
# query = "Who is the CEO of Meta?"
# results = reddit_search.invoke(query)
# print("Results:", results)



'''
pip install stackapi
'''
from langchain_community.tools.stackexchange.tool import StackExchangeTool
from langchain_community.utilities.stackexchange import StackExchangeAPIWrapper

# ✅ Step 1: Create the API wrapper (no API key needed)
api_wrapper = StackExchangeAPIWrapper(site="stackoverflow")

# ✅ Step 2: Use the wrapper inside the tool
stack_exchange = StackExchangeTool(api_wrapper=api_wrapper)

# ✅ Step 3: Run your query
result = stack_exchange.run("python error handling")

print(result)
