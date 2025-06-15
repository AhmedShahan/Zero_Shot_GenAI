'''
No need extra  loader. Just use TextLoader

'''

from langchain_community.document_loaders import TextLoader

loader = TextLoader("/home/shahanahmed/Zero_Shot_GenAI/RAG/1_Document_loader/10_seleniumLoader.py")
docs = loader.load()

print(docs[0].page_content)
