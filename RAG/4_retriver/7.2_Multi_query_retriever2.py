from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_google_genai import ChatGoogleGenerativeAI
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/average_word_embeddings_levy_dependency"
)

all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

VectorStore=Chroma.from_documents(
    embedding=embedding,
    # persist_directory=current_directory,
    collection_name="climate_Change",
    documents=all_docs,
)

query = "How to improve energy levels and maintain balance?"

from langchain.retrievers import MultiQueryRetriever

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)
retriver=MultiQueryRetriever.from_llm(
    retriever=VectorStore.as_retriever(search_kwargs={"k":3}),
    llm=llm
)

result=retriver.invoke(query)
# print(result)
for doc in result:
    print(doc.page_content)