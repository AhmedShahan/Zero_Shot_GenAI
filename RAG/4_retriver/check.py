'''
pip install asknews
'''

from langchain_community.retrievers import AskNewsRetriever

retriever=AskNewsRetriever(
    k=10
)


query="Recent Ai News"

docs=retriever.invoke(query)

# print(docs)
for doc in docs:
    print("Document: ",doc.page_content)
    print("Metadata",doc.metadata)
    print("*"*50)