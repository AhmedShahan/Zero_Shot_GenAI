from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import OllamaLLM, ChatOllama



llm_gemini= GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
llm_chat_gemini= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)
llm_cohere= ChatCohere(model="command-r-plus")
llm_ollama= OllamaLLM(model="deepseek-r1:latest")
llm_chat_ollama= ChatOllama(model="gemma3:latest")

while True:
    prompt= input("You (Type exit to Terminate): ")
    if prompt.lower() == "exit":
        break
    response_gemini= llm_gemini.invoke(prompt)
    response_chat_gemini= llm_chat_gemini.invoke(prompt)
    response_cohere= llm_cohere.invoke(prompt)
    response_ollama= llm_ollama.invoke(prompt)
    response_chat_ollama= llm_chat_ollama.invoke(prompt)

    print("Google LLM Response:", response_gemini)
    print("*"*50)
    print("ChatGoogle LLM Response:", response_chat_gemini.content)
    print("*"*50)
    print("Cohere Response:", response_cohere.content)
    print("*"*50)
    print("Ollama LLM Response:", response_ollama)
    print("*"*50)
    print("ChatOllama LLM Response:", response_chat_ollama.content)