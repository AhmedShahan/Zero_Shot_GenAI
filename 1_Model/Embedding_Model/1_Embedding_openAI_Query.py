from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()  # Load the API key


Embedding=OpenAIEmbeddings(model="text-embedding-3-large", dimensions=100)

result= Embedding.embed_query("What is the capital of Bangladesh?")
print(result)

