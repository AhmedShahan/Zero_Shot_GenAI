from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

from dotenv import load_dotenv
load_dotenv()  # Load the API key

modelGemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)
modelCohera = ChatCohere(model="command-r-plus")
modelLlama = ChatOllama(model="llama3.2:1b")

