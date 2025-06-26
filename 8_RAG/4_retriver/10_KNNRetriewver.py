from langchain.retrievers import KNNRetriever
from langchain.embeddings import HuggingFaceEmbeddings

# Embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Raw documents (texts)
texts = [
    "Dhaka is the capital of Bangladesh.",
    "The Sundarbans is the largest mangrove forest.",
    "Rivers are important to Bangladesh."
]

# Initialize retriever with texts and embedding
retriever = KNNRetriever.from_texts(
    texts=texts,
    embeddings=embedding,
    k=2
)

# Use the retriever
query = "Tell me about forests"
results = retriever.invoke(query)

for doc in results:
    print(doc.page_content)
