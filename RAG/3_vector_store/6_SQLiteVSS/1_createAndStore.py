import sqlite3
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import SQLiteVSS

# Step 1: Load same embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

# Step 2: Connect to the SQLite database manually
db_path = "/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/6_SQLiteVSS/database/players.db"
connection = sqlite3.connect(db_path)

# Step 3: Load the existing table from the connection
vectorStore = SQLiteVSS(
    embedding=embedding,
    connection=connection,
    table="players"  # must match your saved table name
)

# Step 4: Query it
query = "Who is a fast bowler?"
results = vectorStore.similarity_search(query, k=2)

# Step 5: Display results
for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)
