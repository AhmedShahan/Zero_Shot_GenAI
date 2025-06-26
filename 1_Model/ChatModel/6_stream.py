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

# Ask a question
response = llm.stream("Write a short story about a cat in a futuristic city.")
# print(response)

import time
# Streaming Output word by word
# for token in response:
#     print(token.content, end="", flush=True)
#     time.sleep(0.1)

for token in response:
    for char in token.content:
        print(char, end="", flush=True)
        time.sleep(0.05)  # Adjust delay per character