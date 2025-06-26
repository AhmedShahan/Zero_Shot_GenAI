## Here I will Combined all Responces
## Only Chatgot API will be pricing
## Otehrs are free. 

# from langchain import OpenAI, ChatOpenAI, ChatCohere, GoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain_openai import OpenAI, ChatOpenAI
from langchain_cohere import ChatCohere
from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()  # Load the API key

# Initialize the models
llm_openai = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)
llm_chat_openai = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
llm_cohere = ChatCohere(model="command-r-plus")
llm_google = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
llm_chat_google = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

# Function to get responses from all models
prompt="Tell me a joke about a cat."
response_openai = llm_openai.invoke(prompt)
response_chat_openai = llm_chat_openai.invoke(prompt)
response_cohere = llm_cohere.invoke(prompt)
response_google = llm_google.invoke(prompt)
response_chat_google = llm_chat_google.invoke(prompt)
# Print the responses
print("OpenAI LLM Response:", response_openai)
print("*"*50)
print("ChatOpenAI Response:", response_chat_openai.content)
print("*"*50)
print("Cohere Response:", response_cohere.content)
print("*"*50)
print("Google LLM Response:", response_google)
print("*"*50)
print("ChatGoogle LLM Response:", response_chat_google.content)