from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loder=DirectoryLoader(
  
    path="/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/pdfs",
    glob="*.pdf",
    ## direcory থেকে সব pdf file loadd করা
    loader_cls=PyPDFLoader
)


docs=loder.load()

print(len(docs))
### সব গুলো pdf মিলে জোতগুলো পেইজ সেই টোটাল পেইজ নাম্বার 

print(docs[36].page_content)
## 37 Page এর সকল কন্টেন্ট 