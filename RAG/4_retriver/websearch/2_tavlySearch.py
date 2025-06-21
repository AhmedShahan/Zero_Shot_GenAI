'''
pip install tavily-python
'''

from langchain_community.retrievers import TavilySearchAPIRetriever
from dotenv import load_dotenv
load_dotenv()
retriever=TavilySearchAPIRetriever(
    k=10
)


query="Who is the CEO of Meta?"

# docs=retriever.invoke(query)
docs=retriever.get_relevant_documents(query)
print(docs)
# # print(docs)
# for doc in docs:
#     print("Document: ",doc.page_content)
#     print("Metadata",doc.metadata)
#     print("*"*50)