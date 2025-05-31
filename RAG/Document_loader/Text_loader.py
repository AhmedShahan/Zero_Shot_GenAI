from langchain_community.document_loaders import TextLoader

textLoader=TextLoader('/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/text.txt')

docs=textLoader.load()

print(docs)

# print("Type of the Docs: ",type(docs))

# print("Docs Content: ",docs[0].page_content)