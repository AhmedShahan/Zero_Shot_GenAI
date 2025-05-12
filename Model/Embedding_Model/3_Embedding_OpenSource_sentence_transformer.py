from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load the API key




embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")
# All sentence tranformer models are available in HuggingFace Embeddings: https://huggingface.co/sentence-transformers 

text="Dhaka is the capital of Bangladesh. It is the largest city in the country and serves as its political, economic, and cultural center."

vector=embedding.embed_query(text)
print(vector)
