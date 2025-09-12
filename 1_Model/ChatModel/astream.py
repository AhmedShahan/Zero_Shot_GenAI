import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)
import time
stime=time.time()
for chunk in llm.stream("Write a short story about a cat in a futuristic city."):
    print(chunk.content, end="", flush=True)
etime=time.time()

print("Total time:", etime - stime)
###########################  otal time: 17.07764220237732

# import asyncio
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0.5,
# )

# async def main():
#     async for chunk in llm.astream("Write a short story about a robot in space."):
#         print(chunk.content, end="", flush=True)

# import time
# stime=time.time()
# asyncio.run(main())
# etime=time.time()
# print("Total time:", etime - stime)
########### Total time: 13.485547065734863