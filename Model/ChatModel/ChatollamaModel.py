from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-r1:1.5b")

response = llm.invoke("What is the capital of Bangladesh?")

print(response.content)