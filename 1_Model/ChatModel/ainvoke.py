import time
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load the API key

# Initialize the Gemini model using LangChain
# Initialize the Gemini model using LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)
# import time
# stime=time.time()
# response1 = llm.invoke("Tell me a joke about a cat")
# response2 = llm.invoke("Give me a recipe for coffee")
# response3 = llm.invoke("Explain quantum computing simply")
# etime=time.time()
# print(response1.content)
# print(response2.content)
# print(response3.content)
# print("Total Time: ", etime-stime)

################### Total Time:  37.04849171638489 ############
import asyncio
async def main():
    # একসাথে একাধিক query পাঠানো হচ্ছে
    task1 = asyncio.create_task(llm.ainvoke("Tell me a joke about a cat"))
    task2 = asyncio.create_task(llm.ainvoke("Give me a recipe for coffee"))
    task3 = asyncio.create_task(llm.ainvoke("Explain quantum computing simply"))

    # responses = await asyncio.gather(task1, task2, task3)
    # for r in responses:
    #     print("👉", r.content)
    response1=await task1
    response2=await task2
    response3=await task3
    print(response1.content)
stime=time.time()
asyncio.run(main())
etime=time.time()
print("Total Time: ", etime-stime)
###################### Total Time:  14.68141508102417 ################ 