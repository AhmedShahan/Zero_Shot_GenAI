'''
pip install arxiv
'''

from langchain.retrievers import ArxivRetriever

retriever=ArxivRetriever(
    top_k_results=2,
    get_full_documents=True,
    load_all_available_meta=True,

)

query="Authors: Shafin Rahman"

docs=retriever.invoke(query)

# print(docs)
for doc in docs:
    print("Document: ",doc.page_content)
    print("Metadata",doc.metadata)
    print("*"*50)