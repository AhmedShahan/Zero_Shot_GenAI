######  Problem of Vector search and general retriever without argument just top k

from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from  langchain.schema  import Document
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_google_genai import ChatGoogleGenerativeAI
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/average_word_embeddings_levy_dependency"
)


doc1=Document(
    page_content="Climate change is causing glaciers to melt rapidly in the Arctic region.",
    metadata={"topic": "Climate Change"}
)
doc2=Document(
    page_content="Glaciers in the Arctic are melting at an alarming rate due to rising temperatures.",
    metadata={"topic": "Climate Change"}
    )
doc3=Document(
    page_content="Deforestation in the Amazon is accelerating global climate change.",
    metadata={"topic": "Climate Change"}
)
doc4=Document(
    page_content="Climate change is increasing the frequency of wildfires in California.",
    metadata={"topic": "Climate Change"}
)
doc5=Document(
    page_content="Rising sea levels due to climate change threaten coastal cities like Mumbai and New York.",
    metadata={"topic": "Climate Change"}
)

doc6=Document(
    page_content="Sakib Al Hasan gives 5 Million  USD for resolving issues of Climate change issues",
    metadata={"topic":"Sports"}
)
docs=[doc1, doc2, doc3, doc4, doc5,doc6]

current_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/4_retriver"
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)
compressor=LLMChainExtractor.from_llm(llm)

VectorStore=Chroma.from_documents(
    embedding=embedding,
    # persist_directory=current_directory,
    collection_name="climate_Change",
    documents=docs,
)
base_retriever=VectorStore.as_retriever(search_kwargs={"k":3})


compression_retriever= ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor

)

# retriever = VectorStore.as_retriever(
#     search_type="mmr",
#     search_kwargs={"k": 5, "lambda_mult": 0.9}
# )
results = compression_retriever.invoke("Climate change issues")

for doc in results:
    print(doc.page_content)

##  Although doc6 is not  related  to climate change but  it  search and fetch due to sementic  search
##  Its because Climate chnage issues words is directly from the  doc 6