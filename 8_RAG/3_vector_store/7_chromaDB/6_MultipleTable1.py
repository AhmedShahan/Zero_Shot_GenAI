from langchain.vectorstores  import  Chroma
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings


'''
First We have a table called players where there 5 documents. 
'''

doc1=Document(
    page_content="Shakib Al Hasan: One of the best all-rounders in the world, known for his consistent performances with both bat and ball. A pillar of the Bangladesh cricket team for over a decade.",
    metadata={"team":"Fortune Barishal (BPL)"}
)

doc2=Document(
    page_content="Litton Das: A stylish right-handed opener and dependable wicketkeeper. Litton is known for his elegant strokeplay and has become a regular in all formats for Bangladesh.",
    metadata={"team":"Comilla Victorians (BPL)"}
)

doc3=Document(
    page_content="Mustafizur Rahman: Popularly known as The Fizz he is famous for his deceptive cutters and deadly yorkers. A match-winner in death overs.",
    metadata={"team":"Chennai Super Kings (IPL)"}
)


doc4=Document(
    page_content="Towhid Hridoy:  A promising young batsman making a name in international cricket with powerful and composed innings in the middle order.",
    metadata={"team":"Sylhet Strikers (BPL)"}
)

doc5=Document(
    page_content="Taskin Ahmed: A fast bowler with raw pace and energy. Taskin has improved tremendously over the years and is now a key bowler for Bangladesh.",
    metadata={"team":"Dhaka Dominators (BPL)"}
)

sci1 = Document(
    page_content="Dr. Kamrul Hasan is a renowned physicist from Bangladesh. He gained international recognition for his research in nuclear physics.",
    metadata={"sector": "physics"}
)

sci2 = Document(
    page_content="Dr. Sharmin Akter is a distinguished mathematician from Bangladesh. Her main research areas are real analysis and fractal geometry.",
    metadata={"sector": "mathematics"}
)

sci3 = Document(
    page_content="Dr. Rashedul Islam is a computer scientist specializing in artificial intelligence and deep learning. He has made significant contributions to Bangladesh's tech industry.",
    metadata={"sector": "computer science"}
)

sci4 = Document(
    page_content="Dr. Mehzabin Chowdhury is a prominent biologist from Bangladesh. She has conducted extensive research in molecular biology and genetics.",
    metadata={"sector": "biology"}
)

sci5 = Document(
    page_content="Dr. Tariq Anwar is an environmental scientist in Bangladesh. His work focuses on the impacts of climate change on agriculture and coastal communities.",
    metadata={"sector": "environmental science"}
)


players=[doc1, doc2, doc3, doc4, doc5]
scientist=[sci1,sci2,sci3,sci4,sci5]


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

working_dir="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/7_chromaDB/database"

players_store = Chroma(
    embedding_function=embedding,
    persist_directory=working_dir,
    collection_name="players"  # name this collection "players"
)
players_store.add_documents(players)

scientists_store = Chroma(
    embedding_function=embedding,
    persist_directory=working_dir,
    collection_name="scientists"  # name this second collection "scientists"
)
scientists_store.add_documents(scientist)


