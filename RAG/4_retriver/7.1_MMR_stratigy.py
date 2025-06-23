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


# doc1 = Document(page_content="Apple is a fruit that keeps the doctor away.")
# doc2 = Document(page_content="Bananas are rich in potassium.")
# doc3 = Document(page_content="Oranges have a lot of vitamin C.")
# doc4 = Document(page_content="Apple just released a new iPhone.")
# doc5 = Document(page_content="Eating fruits is healthy.")
# docs = [doc1, doc2, doc3, doc4, doc5]



doc1 = Document(page_content="Cats are independent animals.")
doc2 = Document(page_content="Cats love to sleep all day.")
doc3 = Document(page_content="Dogs are loyal animals.")
doc4 = Document(page_content="Parrots can mimic human speech.")
doc5= Document(page_content="Elephants are the largest land animals on Earth.")
docs = [doc1, doc2, doc3, doc4, doc5]

current_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/4_retriver"


VectorStore=Chroma.from_documents(
    embedding=embedding,
    # persist_directory=current_directory,
    collection_name="climate_Change",
    documents=docs,
)
# retriever=VectorStore.as_retriever(search_kwargs={"k":3, "lambda_mult":1}, search_type="mmr")
retriever=VectorStore.as_retriever(search_kwargs={"k":3})



query = "Tell me about animals"
results = retriever.invoke(query)

# ➤ Step 6: Output দেখো
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print("Content:", doc.page_content)