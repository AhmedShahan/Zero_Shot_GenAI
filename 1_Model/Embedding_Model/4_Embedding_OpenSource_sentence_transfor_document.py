from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load the API key




embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text=[
    "Dhaka is the capital of Bangladesh.",
    "Dhaka is the capital of Bangladesh. It is the largest city in the country and serves as its political, economic, and cultural center.",
    "The capital of Bangladesh is Dhaka, which is located in the central part of the country. It is known for its rich history, vibrant culture, and bustling markets.",
]

vector=embedding.embed_documents(text)
print(vector)
