from langchain_community.document_loaders.csv_loader import UnstructuredCSVLoader

# লোডার ইনিশিয়ালাইজ করা
loader = UnstructuredCSVLoader(file_path="/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/bdechonomy2.csv", mode="single")

# ডেটা লোড করা
data = loader.load()

print(data)
# # আউটপুট দেখা
# for doc in data:
#     print(doc.page_content)