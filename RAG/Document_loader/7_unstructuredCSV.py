import pandas as pd

# Clean your CSV file
df = pd.read_csv("your_file.csv", on_bad_lines='skip', engine='python')
df.to_csv("clean_file.csv", index=False)

# Then use UnstructuredCSVLoader
from langchain_community.document_loaders.csv_loader import UnstructuredCSVLoader

loader = UnstructuredCSVLoader("clean_file.csv")
data = loader.load()
print(data[0].page_content)