'''
pip install stackapi
'''
from langchain_community.tools.stackexchange.tool import StackExchangeTool
from langchain_community.utilities.stackexchange import StackExchangeAPIWrapper
from langchain_community.tools import StackExchangeTool


retriever=StackExchangeTool(
    api_wrapper=StackExchangeAPIWrapper(site="datascience")
)

# # ✅ Step 1: Create the API wrapper (no API key needed)
# api_wrapper = StackExchangeAPIWrapper(site="datascience")

# # ✅ Step 2: Use the wrapper inside the tool
# stack_exchange = StackExchangeTool(api_wrapper=api_wrapper)

# ✅ Step 3: Run your query
result = retriever.invoke("python error handling")

print(result)


'''
Site Name	Use in site="..."	Description
Stack Overflow	"stackoverflow"	প্রোগ্রামিং ও সফটওয়্যার ডেভেলপমেন্ট
Super User	"superuser"	Power users ও advanced Windows/Linux ব্যবহারকারী
Ask Ubuntu	"askubuntu"	Ubuntu Linux সম্পর্কিত প্রশ্ন
Unix & Linux	"unix"	অন্যান্য Unix/Linux প্রশ্ন
Mathematics	"math"	Pure & applied math
Cross Validated	"stats"	Statistics, Machine Learning
Data Science	"datascience"	Data science, ML, AI, data analysis
AI Stack Exchange	"ai"	Artificial Intelligence-specific discussions
Server Fault	"serverfault"	SysAdmin ও IT ইনফ্রা প্রশ্ন
Ask Different	"apple"	Apple/macOS/iOS ডিভাইস
Stack Apps	"stackapps"	Stack Exchange API ও অ্যাপ ডেভেলপমেন্ট

'''