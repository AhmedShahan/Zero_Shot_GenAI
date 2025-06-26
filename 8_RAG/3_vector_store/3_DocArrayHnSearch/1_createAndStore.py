from langchain_community.vectorstores import DocArrayHnswSearch
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings


'''
pip install docarray
pip install "docarray[hnswlib]"
'''

# Step 1: Define your documents
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

# Step 3: Define a persistent directory for HNSW index
work_dir = "/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/3_DocArrayHnSearch/database"

# Step 4: Create the vector store
# vectorstore = DocArrayHnswSearch.from_documents(docs, embedding, work_dir=work_dir,n_dim=300)
vectorstore=DocArrayHnswSearch.from_documents(embedding=embedding, documents=docs)

# vectorstore.add_documents(docs)

# # Step 5: Save is implicit; search right away
query = "Who is a powerful middle order batsman?"
results = vectorstore.similarity_search(query, k=2)

# Step 6: Print Results
for res in results:
    print("Matched Content:", res.page_content)
    print("Team:", res.metadata.get('team', 'N/A'))
    print("-" * 60)
