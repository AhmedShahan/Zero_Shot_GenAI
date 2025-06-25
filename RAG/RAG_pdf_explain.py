from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.text_splitter import CharacterTextSplitter

# Load PDF
path = "/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/Electronic Medical Record (EMR) System_Task_Breakdown.pdf"
loader = PyPDFLoader(path)
docs = loader.load()
print(f"Loaded {len(docs)} pages from PDF")

# Split documents
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separator=" ")
all_chunks = []
for doc in docs:
    chunks = splitter.split_documents([doc])
    all_chunks.extend(chunks)
print(f"Total chunks: {len(all_chunks)}")

# Initialize embeddings and vector store
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(embedding_function=embedding, collection_name="sample")

# Add chunks to vector store
vector_store.add_documents(all_chunks)
print(f"Documents in vector store: {vector_store._collection.count()}")

# Initialize LLM and retriever
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
base_retriever = vector_store.as_retriever(search_kwargs={"k": 20})
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(base_retriever=base_retriever, base_compressor=compressor)

# Query and retrieve context
query = "AI related Content"
context = compression_retriever.invoke(query)
print(f"Retrieved {len(context)} documents")

# Define prompt and chain
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
prompt = ChatPromptTemplate.from_messages(MessageRag)
parser = StrOutputParser()
chain = prompt | llm | parser

# Invoke chain
try:
    result = chain.invoke({"question": query, "context": context})
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {str(e)}")