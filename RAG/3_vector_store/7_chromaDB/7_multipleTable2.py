from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/average_word_embeddings_levy_dependency"
)

# Load existing collections
players_store = Chroma(
    embedding_function=embedding,
    persist_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/chromaDB",
    collection_name="players"
)

scientists_store = Chroma(
    embedding_function=embedding,
    persist_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/chromaDB",
    collection_name="scientists"
)

# See number of documents
print("Players:", len(players_store.get()["documents"]))
print("Scientists:", len(scientists_store.get()["documents"]))


# Query within players
query_vec = embedding.embed_query("fast bowler from Bangladesh")
results = players_store.similarity_search_by_vector(query_vec, k=3)
print(results)
# results will only come from the "players" collection

# Query within scientists
query_vec2 = embedding.embed_query("Bangladesh climate change researcher")
results2 = scientists_store.similarity_search_by_vector(query_vec2, k=3)
print(results2)