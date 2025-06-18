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
print(storedElement)

query = "A fast bowler"

results = vector_store.similarity_search(query, k=2)

for doc in results:
    print(doc.page_content)

# result2=vector_store.similarity_search_with_score(query, k=2)

# print(result2)

# for document in  result2:
#     print(document[0].page_content)
#     print("*"*50)


##  Meta data filtering