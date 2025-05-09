from langchain_ollama import Ollama

llm = Ollama(model="deepkeek-r1-14b")

response = llm.invoke("What is the capital of Bangladesh?")

print(response)