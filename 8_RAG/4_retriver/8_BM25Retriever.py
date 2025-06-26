from langchain_community.retrievers import BM25Retriever
from langchain.docstore.document import Document

'''
pip install rank_bm25
'''

# Example documents
documents = [
    Document(page_content="The quick brown fox jumps over the lazy dog"),
    Document(page_content="A fox fled from danger"),
    Document(page_content="The dog sleeps peacefully")
]

retriever = BM25Retriever.from_documents(
    documents=documents,
    k=2  # Number of documents to retrieve
)

query = "fox danger"
documents = retriever.invoke(query)
for doc in documents:
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}\n")