from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Annoy


# Step 2: Initialize embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")



# Optional: Load the index later like this
# Load the FAISS index from disk safely
loaded_vectorstore = Annoy.load_local(
    folder_path="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/2_Annoy",
    embeddings=embedding,
    allow_dangerous_deserialization=True  # Add this line
)


# Search for similar documents
query = "Who is a powerful middle order batsman?"
results = loaded_vectorstore.similarity_search(query, k=2)

for res in results:
    print("Matched Content:", res.page_content)
    print("Team:", res.metadata['team'])
    print("-" * 60)