from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings



embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")



vector_store=Chroma(
    embedding_function=embedding, 
    persist_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/chromaDB",
    collection_name="sample"
)


storedElement=vector_store.get(include=['embeddings','documents','metadatas'])
# print(storedElement)

## metadata wise filter
result=vector_store.similarity_search_with_score(
    query="",
    filter={"team":"Sylhet Strikers (BPL)"}
)

print(result)