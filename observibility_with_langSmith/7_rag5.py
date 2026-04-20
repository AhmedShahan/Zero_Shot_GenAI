from dotenv import load_dotenv
load_dotenv()
import os

os.environ["LANGCHAIN_PROJECT"]="All Tracable RAG 3"
from langsmith import traceable

path = "/media/shahanahmed/c229a233-ed4f-4f67-9e09-5890e65956f7/Zero_Shot_GenAI/8_RAG/documents/islr.pdf"
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
from langchain_community.vectorstores import FAISS

VECTOR_STORE_PATH = "faiss_index"
@traceable(name="Load or Setup Pipeline")
def load_or_setup_pipeline():
    if os.path.exists(VECTOR_STORE_PATH):
        print("Loading existing vector store...")
        emb = embedd()
        return FAISS.load_local(VECTOR_STORE_PATH, emb, allow_dangerous_deserialization=True)
    else:
        print("Setting up pipeline...")
        vs = set_pipeline(pdf_path=path)
        vs.save_local(VECTOR_STORE_PATH)
        return vs


vectorStore = load_or_setup_pipeline()
retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
parallel = RunnableParallel({"context": retriever, "question": RunnablePassthrough()})

# parallel = RunnableParallel({
#     "context": retriever,
#     "question": RunnablePassthrough()
# })

############## Query ###########

### Static Query

# query="What is AI"

# result = chain.invoke(query, config=config)
# print(result)



#### using while Loop


import os



@traceable(name="Query Executions")
def main():

    chain = parallel | prompt | llm | StrOutputParser()
    while True:
        query = input("You: ")
        try:
            result = chain.invoke(query, config={
                "run_name":query
            })
            print(f"Result:\n{result}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
if __name__ == "__main__":
    main()