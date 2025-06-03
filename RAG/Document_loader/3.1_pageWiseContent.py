from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader('/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/pdfs/s41591-024-03057-9.pdf')
docs = loader.load()

# Iterate and print page-wise content
for i, doc in enumerate(docs):
    print(f"\n=== Page {i + 1} ===")
    print("Content:\n", doc.page_content)
    print("Metadata:", doc.metadata)
