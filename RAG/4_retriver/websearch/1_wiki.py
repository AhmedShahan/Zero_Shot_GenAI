######### This code is previously worked but Today not working #########


'''
pip install wikipedia
'''

from langchain_community.retrievers import WikipediaRetriever

retriever=WikipediaRetriever(
    top_k_results=10,
    load_all_available_meta=True
)

query="Who is the CEO of Meta?"

docs=retriever.invoke(query)

# print(docs)
for doc in docs:
    print("Document: ",doc.page_content)
    print("Metadata",doc.metadata)
    print("*"*50)
