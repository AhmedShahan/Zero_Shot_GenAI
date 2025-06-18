### Load a pdf, chunk and Store with embbedding in a seperate folder

from langchain.document_loaders import PyPDFLoader

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


loader=PyPDFLoader("/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/pdfs/Bangladesh.pdf")

docs=loader.load()

# print(docs[0].page_content)


### Split the text means chunking
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    separators=" ",
    chunk_overlap=100
)

chunks=splitter.split_documents(docs)


# print(len(chunks))
# # for chunk in chunks:
# #     print(chunk.page_content)


# for i, chunk in enumerate(chunks):
#     print(f"---- Chunk {i+1} -----")
#     print(chunk.page_content)

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")
vector_store=Chroma(
    embedding_function=embedding, 
    persist_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/chromaDB",
    collection_name="sample"
)

vector_store.add_documents(chunks)
storedElement=vector_store.get(include=['embeddings','documents','metadatas'])
print(storedElement)