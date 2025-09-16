# query.py
from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Initialize Pinecone
pc = Pinecone(api_key="pcsk_6Z5c8A_6HxaqFxzHMHGbnxvWw5mQa43FETCrUfH9mgAqekUCRfZpzeesnsqHqfYUjUkMab")

# 2. Connect to the index
index_name = "cricketer"
index = pc.Index(index_name)

# 3. Load embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Your query
query = "Who is the best all-rounder?"
query_emb = embedding.embed_query(query)

# 5. Query from BD namespace
result_BD = index.query(vector=query_emb, top_k=2, namespace="BD", include_metadata=True)

# 6. Query from PK namespace
result_PK = index.query(vector=query_emb, top_k=2, namespace="PK", include_metadata=True)

print("Bangladesh Search Results:", result_BD)
print("Pakistan Search Results:", result_PK)
