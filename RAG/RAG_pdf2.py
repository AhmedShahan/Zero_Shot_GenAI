path = "/home/shahanahmed/Downloads/Vector Store Recommendations.pdf"


from langchain.document_loaders import PyMuPDFLoader

loader=PyMuPDFLoader(path)
docs = loader.load()
total_page=len(docs)
print(f"Loaded {total_page} pages from PDF")

# for i  in range  (total_page):
#     print(f"Page {i} Content")
#     print(docs[i].page_content)
#     print("*"*50)

############## Text Split 1###########
from langchain.text_splitter import  RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators=" ")
chunks=splitter.split_documents(docs)
total_chunks=len(chunks)
print(f"Total chunks {total_chunks}")

# for  chunk  in chunks:
#     print(chunk.page_content)
#     print("*"*50)

############## Embedding ###########
from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


############## Vector Store ###########
from langchain.vectorstores import Chroma
vector_store = Chroma(embedding_function=embedding, collection_name="sample")

# Add chunks to vector store
vector_store.add_documents(chunks)
print(f"Documents in vector store: {vector_store._collection.count()}")



###########  Retriever ############
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
base_retriever = vector_store.as_retriever(search_kwargs={"k": 20})
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(base_retriever=base_retriever, base_compressor=compressor)

# Query and retrieve context
query = "Vector Store"
context = compression_retriever.invoke(query)
print(f"Retrieved {len(context)} documents")


########### Augmentation #######
MessageRag = [
    ('system', 'You are a Smart AI RAG-based assistant. Please answer the query based on the question.'),
    ('human', '''
     Answer the Question {question} ONLY based on the provided context {context}.
     Please make sure that all the content is available. 
     If the content is insufficient, just say "I don't have enough knowledge based on the document."
     Please Provide Response  Based on this formate. 
     Page Number: 3
     Original Text:  Original Text: AI-Assisted Compliance Auditing
     Use ClinicalBERT/mT5 for diagnosis structuring  
     Build dataset of "spoken → structured note" samples
     ''')
]
from langchain.prompts import ChatPromptTemplate
from  langchain_core.output_parsers import  StrOutputParser
prompt = ChatPromptTemplate.from_messages(MessageRag)
parser = StrOutputParser()
chain = prompt | llm | parser

# Invoke chain
try:
    result = chain.invoke({"question": query, "context": context})
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {str(e)}")
