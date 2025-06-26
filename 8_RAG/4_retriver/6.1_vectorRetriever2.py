from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/average_word_embeddings_levy_dependency"
)


database_path="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/7_chromaDB/database"
# Load existing collections
players_store = Chroma(
    embedding_function=embedding,
    persist_directory=database_path,
    collection_name="players"
)

scientists_store = Chroma(
    embedding_function=embedding,
    persist_directory=database_path,
    collection_name="scientists"
)


retriever=players_store.as_retriever(search_kwargs={"k":2})

query="Who is Sakib Al Hasan"

result=retriever.invoke(query)

print(result)