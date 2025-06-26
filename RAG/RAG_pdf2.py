path = "/home/shahanahmed/Downloads/Vector Store Recommendations.pdf"


from langchain.document_loaders import PyMuPDFLoader

loader=PyMuPDFLoader(path)
docs = loader.load()
total_page=len(docs)
print(f"Loaded {total_page} pages from PDF")

# for i  in range  (total_page):
#     print(f"Page {i} Content")
#     print(docs[i].page_content)
#     print("*"*50)

############## Text Split 1###########
from langchain.text_splitter import  RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators=" ")
chunks=splitter.split_documents(docs)
total_chunks=len(chunks)
print(f"Total chunks {total_chunks}")

# for  chunk  in chunks:
#     print(chunk.page_content)
#     print("*"*50)

############## Embedding ###########
from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


############## Vector Store ###########
from langchain.vectorstores import Chroma
vector_store = Chroma(embedding_function=embedding, collection_name="sample")

# Add chunks to vector store
vector_store.add_documents(chunks)
print(f"Documents in vector store: {vector_store._collection.count()}")
