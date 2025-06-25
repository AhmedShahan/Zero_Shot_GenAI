from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from  langchain_huggingface import HuggingFaceEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
path="/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/Electronic Medical Record (EMR) System_Task_Breakdown.pdf"
loader=PyPDFLoader(path)
# loader=UnstructuredPDFLoader("/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/Electronic Medical Record (EMR) System_Task_Breakdown.pdf")
docs=loader.load()
# print("Docs Content: ",docs[0].page_content)
# print("Metadata: ",docs[0].metadata)


### Split the document. 
from langchain.text_splitter import CharacterTextSplitter
spliter=CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separator=" "
)

all_chunks = []  # To store all chunks

for doc_index, doc in enumerate(docs):
    splited_text = spliter.split_documents(docs)
    print(f"\nDocument {doc_index} has {len(splited_text)} chunks.")
    
    for i, chunk in enumerate(splited_text):
        # print(f"Chunk {i} from Document {doc_index}:")
        # print(chunk)
        # print("*" * 50)
        all_chunks.append(chunk)  # Optional: store for later use


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")
vector_store=Chroma(
    embedding_function=embedding, 
    # persist_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/3_vector_store/chromaDB",
    collection_name="sample"
)

from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)
base_retriever = vector_store.as_retriever(search_kwargs={"k": 5})
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

query = "AI related Content"
compressed_results = compression_retriever.invoke(query)
for doc in  compressed_results:
    print(doc)