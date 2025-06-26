path = "/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/Electronic Medical Record (EMR) System_Task_Breakdown.pdf"


from langchain.document_loaders import UnstructuredPDFLoader

loader=UnstructuredPDFLoader(path)
docs = loader.load()
total_page=len(docs)
print(f"Loaded {total_page} pages from PDF")

# for i  in range  (total_page):
#     print(f"Page {i} Content")
#     print(docs[i].page_content)
#     print("*"*50)

############## Text Split ###########
from langchain.text_splitter import  CharacterTextSplitter
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separator=" ")
chunks=splitter.split_documents(docs)
total_chunks=len(chunks)
print(f"Total chunks {total_chunks}")

for  chunk  in chunks:
    print(chunk.page_content)
    print("*"*50)