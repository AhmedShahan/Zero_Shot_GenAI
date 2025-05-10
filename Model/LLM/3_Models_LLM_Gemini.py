#### Gemini LLMs ####

'''
pip install langchain langchain-google-genai google-generativeai 
'''

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load the API key

# Initialize the Gemini model using LangChain
# Initialize the Gemini model using LangChain
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)

# Ask a question
response = llm.invoke("wHAT IS THE CAPITAL OF bANGLADESH? ")
print(response)