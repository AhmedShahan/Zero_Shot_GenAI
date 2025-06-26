from langchain_google_genai  import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


### Load  the  ddodcument  / txt file
from langchain_community.document_loaders import  TextLoader

loader=TextLoader("/media/ahmedshahan/b8c6fb5d-b937-4730-bb0f-ac0eba675d7e/Zero_Shot_GenAI/RAG/documents/text2.txt") 
docs=loader.load()

print(docs[0].page_content)



from langchain_text_splitters import RecursiveCharacterTextSplitter


splitters=RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,   
    separators=" "
)

chunk=splitters.split_text(docs[0].page_content)
print(chunk)
