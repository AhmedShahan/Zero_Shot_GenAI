from langchain_community.vectorstores import DocArrayHnswSearch
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import DocArrayHnswSearch
from langchain_huggingface import HuggingFaceEmbeddings

print("load_local" in dir(DocArrayHnswSearch))


'''
There is no way to load the database

'''
# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")
# work_dir = "/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/DocArrayHnsw"

# vectorstore = DocArrayHnswSearch.load_local(
#     work_dir=work_dir,
#     embedding=embedding,
#     n_dim=300  # required
# )



# # Search for similar documents
# query = "Who is a powerful middle order batsman?"
# results = vectorstore.similarity_search(query, k=2)

# for res in results:
#     print("Matched Content:", res.page_content)
#     print("Team:", res.metadata['team'])
#     print("-" * 60)