import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import SQLiteVSS
from langchain.docstore.document import Document

# Step 1: Define documents
doc1 = Document(
    page_content="Shakib Al Hasan: One of the best all-rounders in the world, known for his consistent performances with both bat and ball. A pillar of the Bangladesh cricket team for over a decade.",
    metadata={"team": "Fortune Barishal (BPL)"}
)
doc2 = Document(
    page_content="Litton Das: A stylish right-handed opener and dependable wicketkeeper. Litton is known for his elegant strokeplay and has become a regular in all formats for Bangladesh.",
    metadata={"team": "Comilla Victorians (BPL)"}
)
doc3 = Document(
    page_content="Mustafizur Rahman: Popularly known as The Fizz he is famous for his deceptive cutters and deadly yorkers. A match-winner in death overs.",
    metadata={"team": "Chennai Super Kings (IPL)"}
)
doc4 = Document(
    page_content="Towhid Hridoy: A promising young batsman making a name in international cricket with powerful and composed innings in the middle order.",
    metadata={"team": "Sylhet Strikers (BPL)"}
)
doc5 = Document(
    page_content="Taskin Ahmed: A fast bowler with raw pace and energy. Taskin has improved tremendously over the years and is now a key bowler for Bangladesh.",
    metadata={"team": "Dhaka Dominators (BPL)"}
)

docs = [doc1, doc2, doc3, doc4, doc5]

# Step 2: Initialize embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

# Step 3: Ensure the directory exists and use an absolute path for the database
db_dir = "/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/6_SQLiteVSS/database"
db_file = os.path.join(db_dir, "players.db")

# Create the directory if it doesn't exist
os.makedirs(db_dir, exist_ok=True)

# Step 4: Initialize SQLiteVSS vector store
vectorStore=SQLiteVSS.from_documents(
        documents=docs,
        embedding=embedding,
        table="players",
        # db_file=db_file

)
query = "Who is a key bowler for Bangladesh?"

result=vectorStore.similarity_search_with_score(query=query)
print(result)

