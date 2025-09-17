# query.py
from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings

pc = Pinecone(api_key="pcsk_6Z5c8A_6HxaqFxzHMHGbnxvWw5mQa43FETCrUfH9mgAqekUCRfZpzeesnsqHqfYUjUkMab")
index = pc.Index("cricketer")

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query = "Tell me about bowler"
query_emb = embedding.embed_query(query)

# 🚨 No namespace → searches entire index
result = index.query(vector=query_emb, top_k=2, include_metadata=True)

print("Search Results:", result)
