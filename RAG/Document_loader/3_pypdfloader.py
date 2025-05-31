'''
`pip install pypdf
'''
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/AboutBangladesh.pdf')
docs=loader.load()

print(docs)
