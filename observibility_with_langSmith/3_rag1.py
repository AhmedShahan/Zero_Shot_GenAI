import os
os.environ["LANGCHAIN_PROJECT"]="RAG 1"

config={
    "run_name":"Basic RAG Version 1",
    "tags":["llm-app", "rag", "naive rag", "QA"],
    "metadata":{
        "model":"llama-3.1-8b-instent", 
        "temperature":0.7, 
        "parser":"stroutputparser", 
        "pdf_loader":"PyMuPDFLoader", 
        "embedding":"sentence-transformers/average_word_embeddings_levy_dependency",
        "vector_db":"FAISS",
        "search_type": "similarity"
        }
}

path = "/media/shahanahmed/c229a233-ed4f-4f67-9e09-5890e65956f7/Zero_Shot_GenAI/8_RAG/documents/AboutBangladesh.pdf"
from langchain_community.document_loaders import PyMuPDFLoader
loader=PyMuPDFLoader(path)
docs = loader.load()
total_page=len(docs)
print(f"Loaded {total_page} pages from PDF")

# for i  in range  (total_page):
#     print(f"Page {i} Content")
#     print(docs[i].page_content)
#     print("*"*50)

############## Text Split 1###########
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators=" ")
chunks=splitter.split_documents(docs)
total_chunks=len(chunks)
print(f"Total chunks {total_chunks}")

# for  chunk  in chunks:
#     print(chunk.page_content)
#     print("*"*50)

############## Embedding ###########
from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")



############## Vector Store ###########
from langchain_community.vectorstores import FAISS
vector_store = FAISS.from_documents(chunks, embedding)




###########  Retriever ############
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})



########### Augmentation #######

from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

MessageRag = [
    ('system', 'You are a Smart AI RAG-based assistant. Please answer the query based on the question.'),
    ('human', '''
     Answer the Question {question} ONLY based on the provided context {context}.
     Please make sure that all the content is available. 
     If the content is insufficient, just say "I don't have enough knowledge based on the document."
     ''')
]

############## Chain ###########
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
prompt=ChatPromptTemplate.from_messages(MessageRag)
parser = StrOutputParser()

chain = prompt | llm | parser

############## Query ###########

# while True:
# query = input("Enter your Query: ")
query="What is AI"
context_docs = retriever.invoke(query)
# context = format_docs(context_docs)
print(f"Retrieved {len(context_docs)} documents")
try:
    result = chain.invoke({"question": query, "context": context_docs}, config=config)
    print(f"Result:\n{result}")
except Exception as e:
    print(f"Error: {str(e)}")
