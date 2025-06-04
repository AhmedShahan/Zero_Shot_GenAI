from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/AboutBangladesh.pdf")

docs=loader.load()
print(docs[0].page_content)


### Split the document. 
from langchain.text_splitter import CharacterTextSplitter
spliter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=" "
)

splited_text=spliter.split_text(docs[0].page_content)

print("Total Chunk: ",len(splited_text))
for i in range (len(splited_text)):
    print("Chunk: ",i)
    print(splited_text[i])
    print("*"*50)