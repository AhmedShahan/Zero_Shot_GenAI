from langchain_community.vectorstores import SKLearnVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
import numpy as np

# Step 1: Load embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

# Step 2: Define documents
docs = [
    Document(
        page_content="Shakib Al Hasan: One of the best all-rounders in the world, known for his consistent performances with both bat and ball. A pillar of the Bangladesh cricket team for over a decade.",
        metadata={"team": "Fortune Barishal (BPL)"}
    ),
    Document(
        page_content="Litton Das: A stylish right-handed opener and dependable wicketkeeper. Litton is known for his elegant strokeplay and has become a regular in all formats for Bangladesh.",
        metadata={"team": "Comilla Victorians (BPL)"}
    ),
    Document(
        page_content="Mustafizur Rahman: Popularly known as The Fizz he is famous for his deceptive cutters and deadly yorkers. A match-winner in death overs.",
        metadata={"team": "Chennai Super Kings (IPL)"}
    ),
    Document(
        page_content="Towhid Hridoy:  A promising young batsman making a name in international cricket with powerful and composed innings in the middle order.",
        metadata={"team": "Sylhet Strikers (BPL)"}
    ),
    Document(
        page_content="Taskin Ahmed: A fast bowler with raw pace and energy. Taskin has improved tremendously over the years and is now a key bowler for Bangladesh.",
        metadata={"team": "Dhaka Dominators (BPL)"}
    )
]

# Step 2: Load the embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

# Step 4: Create the vector store
working_dir="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/5_SKLearnVectorStore/database"
vectorstore = SKLearnVectorStore(
    embedding=embedding,
    persist_path=working_dir,  
)
# vectorstore.add(docs)
# vectorstore.save_local("/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/FAISS/faiss_db")

# Step 5: Search with a query
query = "Who is a strong middle order batsman?"

results = vectorstore.similarity_search(query, k=2)



# Step 6: Show results
for res in results:
    print("Matched Content:", res.page_content)
    print("Team:", res.metadata.get('team', 'N/A'))
    print("-" * 60)
