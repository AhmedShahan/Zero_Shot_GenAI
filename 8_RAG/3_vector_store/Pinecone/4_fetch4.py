# query.py
from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings

pc = Pinecone(api_key="pcsk_6Z5c8A_6HxaqFxzHMHGbnxvWw5mQa43FETCrUfH9mgAqekUCRfZpzeesnsqHqfYUjUkMab")
index = pc.Index("cricketer")

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query = "Who is Shakib Al Hasan?"
query_emb = embedding.embed_query(query)

namespaces = ["BD", "PK"]
all_results = []

for ns in namespaces:
    result = index.query(
        vector=query_emb,
        top_k=2,
        include_metadata=True,
        namespace=ns
    )
    all_results.extend(result["matches"])

# Optional: sort by score to get overall top-k
all_results = sorted(all_results, key=lambda x: x["score"], reverse=True)[:2]

print("Top results across all namespaces:", all_results)

