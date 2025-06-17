'''
pip install wikipedia
'''

from langchain_community.retrievers import WikipediaRetriever

retriever=WikipediaRetriever(
    top_k_results=10,
)

query="Who is the CEO of Meta?"

docs=retriever.invoke(query)

print(docs)