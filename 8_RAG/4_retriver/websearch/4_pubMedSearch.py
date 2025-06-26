'''
pip install xmltodict
'''

from langchain.retrievers import PubMedRetriever

retriever = PubMedRetriever(
    top_k_results=10
)

query="Authors: Shafin Rahman"

docs=retriever.invoke(query)

print(docs)
# for doc in docs:
#     print("Document: ",doc.page_content)
#     print("Metadata",doc.metadata)
#     print("*"*50)