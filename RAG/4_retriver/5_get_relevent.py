from langchain_community.retrievers import ArxivRetriever

# Initialize retriever
retriever = ArxivRetriever(top_k_results=10)

# Query arXiv
docs = retriever.get_relevant_documents("Shafin Rahman")

# Print results
for doc in docs:
    print("Title:", doc.metadata.get("Title", "N/A"))
    print("Authors:", doc.metadata.get("Authors", "N/A"))
    print("Publish Year",doc.metadata.get("Published"))
    print("Summary:", doc.page_content[:300], "...\n")
