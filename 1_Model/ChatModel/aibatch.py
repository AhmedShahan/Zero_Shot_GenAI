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
query=[
    "Write a short story about a cat in a futuristic city.",
    "Describe a dog who became president in the year 3000.",
    "What would a coffee shop on Mars be like?",
    "Tell me a bedtime story involving a robot and a sunflower."
]
import time 
# stime=time.time()
# responses = llm.batch(query)
# for response in responses:
#     print(response.content)
#     print("*"*50)
# etime=time.time()
# print("Total Time: ", etime-stime)

############# Total Time:  5.465405464172363
import asyncio
async def main():
    prompts = [
        "Summarize the story of Hamlet",
        "What is the capital of France?",
        "Write a haiku about the ocean"
    ]
    responses = await llm.abatch(prompts)
    for r in responses:
        print("👉", r.content)
stime=time.time()

asyncio.run(main())
etime=time.time()
print("Total Time: ", etime-stime)

############ Total Time:  2.4246623516082764