from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings

# Embedding function
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Dummy docs
docs = [
    Document(page_content="Shakib Al Hasan is a great cricketer."),
    Document(page_content="Tamim Iqbal is known for aggressive batting."),
]

# ✅ Create the vectorstore using `from_documents()` first with empty list
# vectorstore = DocArrayInMemorySearch.from_documents([], embedding=embedding)
vectorstore = DocArrayInMemorySearch.from_documents(embedding=embedding, documents=docs)


# ➕ Then add documents using add_documents()
# vectorstore.add_documents(docs)

# 🔍 Perform a similarity search
query = "Who is a famous cricketer?"
results = vectorstore.similarity_search(query, k=2)

for doc in results:
    print(doc.page_content)
