from langchain_core.tools import tool

from langchain_core.tools import tool

@tool
def ArxiveTool(query: str, k: int, full_document: bool = False, load_all_meta: bool = False) -> list:
    """Fetch Document from Arxiv using Arxiv Retriever"""
    from langchain.retrievers import ArxivRetriever

    retriever = ArxivRetriever(
        top_k_results=k,
        get_full_documents=full_document,
        load_all_available_meta=load_all_meta,
    )
    docs = retriever.invoke(query)
    return docs


query= "Paper of Shafin Rahman"
results=ArxiveTool.invoke({
    "query": query,
    "k":3
})

for doc in results:
    print(doc.metadata["Title"])