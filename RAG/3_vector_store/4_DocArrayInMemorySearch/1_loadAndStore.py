from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

'''
pip install docarray
'''

# Step 1: Load the embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

# Step 2: Define your documents
docs = [
    Document(page_content="Shakib Al Hasan is a world-class all-rounder.", metadata={"team": "Fortune Barishal"}),
    Document(page_content="Litton Das is a stylish opener from Bangladesh.", metadata={"team": "Comilla Victorians"}),
    Document(page_content="Towhid Hridoy is a powerful middle-order batsman.", metadata={"team": "Sylhet Strikers"})
]

# Step 3: Create the in-memory vector store
vectorstore = DocArrayInMemorySearch.from_documents(docs, embedding)
vectorstore.save_local("/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/4_DocArrayInMemorySearch")
# Step 4: Perform a similarity search
query = "Who is a strong middle order batsman?"
results = vectorstore.similarity_search(query, k=2)

# Step 5: Show results
for res in results:
    print("Matched Content:", res.page_content)
    print("Team:", res.metadata.get('team', 'N/A'))
    print("-" * 60)
