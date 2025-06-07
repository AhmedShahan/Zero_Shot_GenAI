# Method 1: Most Simple - Direct loading and printing
from langchain.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="/media/ahmedshahan/b8c6fb5d-b937-4730-bb0f-ac0eba675d7e/Zero_Shot_GenAI/RAG/documents",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

# Simple approach - just print everything
current_source = None
page_num = 1

for doc in docs:
    if doc.metadata['source'] != current_source:
        current_source = doc.metadata['source']
        page_num = 1
        print(f"\n{'='*50}")
        print(f"FILE: {current_source}")
        print(f"{'='*50}")
    
    print(f"\n--- Page {page_num} ---")
    print(doc.page_content)
    page_num += 1

print("\n" + "="*50)

# Method 2: One-liner approach (if you just want to see content)
# for i, doc in enumerate(docs):
#     print(f"\nDoc {i+1} ({doc.metadata['source']}):\n{doc.page_content}\n{'-'*50}")

# Method 3: If you want to save to files instead of printing
# import os
# for doc in docs:
#     filename = os.path.basename(doc.metadata['source']).replace('.pdf', '.txt')
#     with open(f"extracted_{filename}", 'a', encoding='utf-8') as f:
#         f.write(doc.page_content + "\n\n")