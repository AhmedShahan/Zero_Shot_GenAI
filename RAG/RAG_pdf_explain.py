from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from  langchain_huggingface import HuggingFaceEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader, PyPDFLoader
path="/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/Electronic Medical Record (EMR) System_Task_Breakdown.pdf"
loader=PyPDFLoader(path)
# loader=UnstructuredPDFLoader("/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/Electronic Medical Record (EMR) System_Task_Breakdown.pdf")
docs=loader.load()
print("Docs Content: ",docs[0].page_content)
print("Metadata: ",docs[0].metadata)