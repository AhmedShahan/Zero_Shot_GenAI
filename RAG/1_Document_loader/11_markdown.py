'''
pip install unstructured[md]
'''

from langchain_community.document_loaders import UnstructuredMarkdownLoader

loader=UnstructuredMarkdownLoader("/home/shahanahmed/Zero_Shot_GenAI/RAG/documents/markddownFile.md")

docs=loader.load()
print(docs[0].page_content)