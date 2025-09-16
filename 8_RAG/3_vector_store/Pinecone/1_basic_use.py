from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone as PineconeStore
from pinecone import Pinecone


from pinecone import Pinecone, ServerlessSpec
import pinecone

pc = Pinecone(api_key="pcsk_6Z5c8A_6HxaqFxzHMHGbnxvWw5mQa43FETCrUfH9mgAqekUCRfZpzeesnsqHqfYUjUkMab")


index_name="cricketer"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # all-MiniLM-L6-v2 outputs 384-dim vectors
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
index = pc.Index(index_name)
docs_BD = [
    Document(page_content="Shakib Al Hasan is one of the best all-rounders.", metadata={"team": "Bangladesh"}),
    Document(page_content="Litton Das is a stylish right-handed opener.", metadata={"team": "Bangladesh"})
]
docs_PK = [
    Document(page_content="Babar Azam is one of the finest batsmen in modern cricket.", metadata={"team": "Pakistan"}),
    Document(page_content="Shaheen Afridi is a left-arm fast bowler known for his deadly swing.", metadata={"team": "Pakistan"})
]
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorsBD = []
for i, doc in enumerate(docs_BD):
    emb = embedding.embed_query(doc.page_content)
    vectorsBD.append({
        "id": f"doc{i}",
        "values": emb,
        "metadata": doc.metadata
    })
vectorsPK = []
for i, doc in enumerate(docs_PK):
    emb = embedding.embed_query(doc.page_content)
    vectorsPK.append({
        "id": f"doc{i}",
        "values": emb,
        "metadata": doc.metadata
    })



index.upsert(vectors=vectorsBD, namespace="BD")
index.upsert(vectors=vectorsPK, namespace="PK")