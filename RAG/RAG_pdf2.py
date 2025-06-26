path = "/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/Electronic Medical Record (EMR) System_Task_Breakdown.pdf"


from langchain.document_loaders import PyPDFLoader

loader=PyPDFLoader(path)
docs = loader.load()
total_page=len(docs)
print(f"Loaded {total_page} pages from PDF")

for i  in range  (total_page):
    print(f"Page {i} Content")
    print(docs[i].page_content)
    print("*"*50)
