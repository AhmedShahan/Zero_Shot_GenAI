from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec
import os
from pinecone import Pinecone
from dotenv import load_dotenv
# Load .env
load_dotenv()
# Initialize Pinecone
api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key)

index_name = "cricketer"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # all-MiniLM-L6-v2 outputs 384-dim vectors
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

# Documents
docs_BD = [
    Document(page_content="Shakib Al Hasan is one of the best all-rounders and left bowler.", metadata={"team": "Bangladesh"}),
    Document(page_content="Litton Das is a stylish right-handed opener.", metadata={"team": "Bangladesh"})
]
docs_PK = [
    Document(page_content="Babar Azam is one of the finest batsmen in modern cricket.", metadata={"team": "Pakistan"}),
    Document(page_content="Shaheen Afridi is a left-arm fast bowler known for his deadly swing.", metadata={"team": "Pakistan"})
]

# Embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Prepare BD vectors
vectorsBD = []
for i, doc in enumerate(docs_BD):
    emb = embedding.embed_documents([doc.page_content])[0]   # ✅ FIX
    vectorsBD.append({
        "id": f"BD_doc{i}",
        "values": emb,
        "metadata": {"team": doc.metadata["team"], "text": doc.page_content}
    })

# Prepare PK vectors
vectorsPK = []
for i, doc in enumerate(docs_PK):
    emb = embedding.embed_documents([doc.page_content])[0]   # ✅ FIX
    vectorsPK.append({
        "id": f"PK_doc{i}",
        "values": emb,
        "metadata": {"team": doc.metadata["team"], "text": doc.page_content}
    })

# Upsert into Pinecone
index.upsert(vectors=vectorsBD, namespace="BD")
index.upsert(vectors=vectorsPK, namespace="PK")

print("✅ Vectors inserted successfully")

# Optional: check stats
print(index.describe_index_stats())
