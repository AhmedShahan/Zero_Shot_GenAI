from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

wiki = WikipediaAPIWrapper(top_k_results=10, lang="en")

query = "Who is the CEO of Meta?"
results = wiki.run(query)

print("Results:\n", results)