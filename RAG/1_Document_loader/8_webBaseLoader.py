from langchain_community.document_loaders import WebBaseLoader
url="https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/","https://ahmedshahan.github.io" 
loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))

print(docs[1].page_content)