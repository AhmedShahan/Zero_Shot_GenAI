from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load the API key




embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="Dhaka is the capital of Bangladesh. It is the largest city in the country and serves as its political, economic, and cultural center."

vector=embedding.embed_query(text)
print(vector)
