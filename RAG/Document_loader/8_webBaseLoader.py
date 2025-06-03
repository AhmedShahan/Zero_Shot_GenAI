from langchain_community.document_loaders import WebBaseLoader
url="https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/"
loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))

# print(docs[0].page_content)