from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from collections import defaultdict

# Load all PDFs in the directory
loader = DirectoryLoader(
    path="/media/ahmedshahan/b8c6fb5d-b937-4730-bb0f-ac0eba675d7e/Zero_Shot_GenAI/RAG/documents",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# Load all pages
docs = loader.load()

# Group pages by source file
pdf_docs = defaultdict(list)
for doc in docs:
    pdf_docs[doc.metadata['source']].append(doc)

# Print content grouped by PDF file and then by page
for pdf_file, pages in pdf_docs.items():
    print(f"\n==================== {pdf_file} ====================\n")
    for i, page in enumerate(pages, start=1):
        print(f"\n--- Page {i} Content ---\n")
        print(page.page_content)
