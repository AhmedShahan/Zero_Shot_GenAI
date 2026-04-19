from dotenv import load_dotenv
load_dotenv()
import os

os.environ["LANGCHAIN_PROJECT"]="All Tracable RAG"
from langsmith import traceable
config={
    "run_name":"Basic RAG Version 2",
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

@traceable(name="Load Pdf", tags=["pdf load","PyMuPDFLoader"], metadata={
    "Input":"Pdf path",
    "PDF Loader":"PyMuPDFLoader",
    "Return":"Docs"
})
def load_pdf(path:str):
    loader=PyMuPDFLoader(path)
    docs = loader.load()
    total_page=len(docs)
    print(f"Loaded {total_page} pages from PDF")

    return docs 


############## Text Split 1###########
from langchain_text_splitters import RecursiveCharacterTextSplitter
@traceable(name="Split Text", metadata={
    "Input":"Docs",
    "chunk_size":1000,
    "chunk_overlap":100,
    "serator":"word By Word",
    "Return":"Chunks"
})
def split_text(docs, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separators=" ")
    chunks=splitter.split_documents(docs)
    total_chunks=len(chunks)
    print(f"Total chunks {total_chunks}")

    return chunks




############## Embedding ###########
@traceable(name="Embedding", metadata={
    "Input": "Nothing",
    "Provider":"HuggingFace",
    "model_name":"sentence-transformers/average_word_embeddings_levy_dependency",
    "return": "Embeddiing model"
})
def embedd(model_name="sentence-transformers/average_word_embeddings_levy_dependency"):
    from langchain_huggingface import HuggingFaceEmbeddings
    embedding = HuggingFaceEmbeddings(model_name=model_name)

    return embedding


############## Vector Store ###########
@traceable(name="Vector Store",metadata={
    "Input": "Chunk, embedding model",
    "vector_store":"FAISS",
    "Return":"Vector Store"

})
def vector_store(chunks, embedding):
    from langchain_community.vectorstores import FAISS
    vector_store = FAISS.from_documents(chunks, embedding)

    return vector_store

@traceable(name="Setup Pipeline", metadata={
    "Input":"pdf path",
    "Process": "Load_df-> split->embed",
    "return":"Vector Store"
})
def set_pipeline(pdf_path:str):
    docs=load_pdf(pdf_path)
    splits=split_text(docs)
    emb=embedd()
    vs=vector_store(splits,emb)
    
    return vs


###########  Retriever ############

vectorStore=set_pipeline(pdf_path=path)
retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k": 4})



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

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel,  RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
prompt=ChatPromptTemplate.from_messages(MessageRag)
parser = StrOutputParser()


parallel = RunnableParallel({
    "context": retriever,
    "question": RunnablePassthrough()
})

chain = parallel | prompt | llm | StrOutputParser()

############## Query ###########

### Static Query

# query="What is AI"

# result = chain.invoke(query, config=config)
# print(result)



#### using while Loop
while True:
    query=input("You: ")
    try:
        result = chain.invoke(query, config=config)
        print(f"Result:\n{result}")
    except Exception as e:
        print(f"Error: {str(e)}")
