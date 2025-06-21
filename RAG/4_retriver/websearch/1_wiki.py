'''
pip install wikipedia
'''

from langchain.retrievers  import WikipediaRetriever

retriever=WikipediaRetriever(
    top_k_results=10,
    # load_all_available_meta=True
)

query="Who is the CEO of Meta?"

docs=retriever.invoke(query)
# docs=retriever.get_relevant_documents(query)

# print(docs)
for doc in docs:
    print("Document: ",doc.page_content)
    print("Metadata",doc.metadata)
    print("*"*50)








