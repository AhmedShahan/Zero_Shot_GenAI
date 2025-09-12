# import asyncio
# from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
# from dotenv import load_dotenv
# load_dotenv()
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.5
# )

# async def main():
#     async for chunk in llm.astream("Write a short story about a robot in space."):
#         print(chunk.content, end="", flush=True)

# asyncio.run(main())



import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5
)

async def main():
    async for chunk in llm.astream("Write a short story about a robot in space."):
        text = chunk.content or ""
        for char in text:
            print(char, end="", flush=True)
            await asyncio.sleep(0.05)  # adjust speed here

asyncio.run(main())
