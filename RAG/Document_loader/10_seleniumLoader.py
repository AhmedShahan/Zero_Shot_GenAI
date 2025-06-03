from langchain_community.document_loaders import SeleniumURLLoader

url=["https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/","https://www.daraz.com.bd/#?","https://ahmedshahan.github.io/first.html"]

loader=SeleniumURLLoader(url)


docs=loader.load()

print(docs)