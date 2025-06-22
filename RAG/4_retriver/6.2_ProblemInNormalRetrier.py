######  Problem of Vector search and general retriever without argument just top k

from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from  langchain.schema  import Document
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/average_word_embeddings_levy_dependency"
)
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

docs=[doc1, doc2, doc3, doc4, doc5]

current_directory="/home/shahanahmed/Zero_Shot_GenAI/RAG/4_retriver"

VectorStore=Chroma.from_documents(
    embedding=embedding,
    # persist_directory=current_directory,
    collection_name="Climate_Change",
    documents=docs,
)



