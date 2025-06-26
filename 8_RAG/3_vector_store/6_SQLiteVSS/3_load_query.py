import os
import sqlite3
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import SQLiteVSS

# Step 1: Initialize embeddings (must match the model used when creating the vector store)
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

# Step 2: Specify the database file path
db_file = "/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/6_SQLiteVSS/database"
table_name = "players.db"

# Step 3: Create a SQLite connection
try:
    connection = sqlite3.connect(db_file)
except Exception as e:
    print(f"Error creating SQLite connection: {e}")
    exit()

# Step 4: Load the SQLiteVSS vector store
try:
    db = SQLiteVSS(
        table=table_name,
        connection=connection,
        embedding=embedding
    )
except Exception as e:
    print(f"Error loading vector store: {e}")
    connection.close()
    exit()

# Step 5: Perform a similarity search
query = "Who is a key bowler for Bangladesh?"
try:
    results = db.similarity_search(query, k=2)  # Retrieve top 2 most similar documents
    print("Query Results:")
    for i, doc in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Content: {doc.page_content}")
        print(f"Metadata: {doc.metadata}")
except Exception as e:
    print(f"Error performing similarity search: {e}")
finally:
    connection.close()  # Close the connection after use
