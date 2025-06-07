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

# প্রথমে দুইটা variable তৈরি করি
current_source = None  # এখানে রাখবো বর্তমানে কোন PDF file টা process করছি
page_num = 1          # page number count করার জন্য

# এখন সব documents এর মধ্যে loop চালাই
for doc in docs:  # docs হচ্ছে সব PDF pages এর list
    
    # Check: এই document টা কি নতুন PDF file এর?
    if doc.metadata['source'] != current_source:
        # যদি নতুন file হয়, তাহলে:
        current_source = doc.metadata['source']  # নতুন file name save করি
        page_num = 1                            # page number আবার 1 থেকে শুরু
        
        # নতুন file এর header print করি
        print(f"\n{'='*50}")                   # 50টা = চিহ্ন দিয়ে line
        print(f"FILE: {current_source}")       # file এর name
        print(f"{'='*50}")                     # আবার 50টা = চিহ্ন
    
    # এখন page এর content print করি
    print(f"\n--- Page {page_num} ---")        # page number দেখাই
    print(doc.page_content)                    # page এর actual content
    page_num += 1                              # next page এর জন্য number বাড়াই

# সব শেষে একটা final line
print("\n" + "="*50)

# উদাহরণ: 
# ধরি আপনার কাছে 2টা PDF আছে: book1.pdf (2 pages), book2.pdf (3 pages)
# Output দেখাবে এরকম:

# ==================================================
# FILE: /path/book1.pdf
# ==================================================
# 
# --- Page 1 ---
# [book1 এর page 1 এর content]
# 
# --- Page 2 ---
# [book1 এর page 2 এর content]
# 
# ==================================================
# FILE: /path/book2.pdf  
# ==================================================
# 
# --- Page 1 ---
# [book2 এর page 1 এর content]
# 
# --- Page 2 ---
# [book2 এর page 2 এর content]
# 
# --- Page 3 ---
# [book2 এর page 3 এর content]
# 
# ==================================================