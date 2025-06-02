import pandas as pd
import pdfplumber

all_tables = []

with pdfplumber.open("/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/tabular_text.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

# সব টেবিল একসাথে প্রিন্ট
for idx, table_df in enumerate(all_tables):
    print(f"\n🔹 Table {idx+1}:\n", table_df)
