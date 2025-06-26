from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()  # Load the API key
documents=["Dhaka is the capital of Bangladesh.",
              "Dhaka is the capital of Bangladesh. It is the largest city in the country and serves as its political, economic, and cultural center.",
                "The capital of Bangladesh is Dhaka, which is located in the central part of the country. It is known for its rich history, vibrant culture, and bustling markets.",
           ]

Embedding=OpenAIEmbeddings(model="text-embedding-3-large", dimensions=100)

result= Embedding.embed_documents(documents)
print(result)

