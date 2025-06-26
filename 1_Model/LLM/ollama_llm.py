from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b")

response = llm.invoke("What is the capital of Bangladesh?")

print(response)