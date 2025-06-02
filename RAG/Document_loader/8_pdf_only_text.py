from langchain.document_loaders import UnstructuredPDFLoader
from unstructured.partition.pdf import partition_pdf
import pandas as pd
import re


def extract_text_paragraphs(elements):
    paragraphs = []
    current_paragraph = ""

    for element in elements:
        if element.category in ["Table", "TableChunk", "ListItem"]:
            continue

        if element.category in ["Text", "NarrativeText"]:
            text = str(element).strip()
            if not text:
                continue

            if current_paragraph:
                if current_paragraph[-1] in ".!?" and text[0].isupper():
                    paragraphs.append(current_paragraph.strip())
                    current_paragraph = text
                else:
                    current_paragraph += " " + text
            else:
                current_paragraph = text

    if current_paragraph:
        paragraphs.append(current_paragraph.strip())

    # Clean and filter
    cleaned_paragraphs = []
    for para in paragraphs:
        cleaned = re.sub(r'\s+', ' ', para).strip()
        cleaned = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', cleaned)
        cleaned = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', cleaned)
        if len(cleaned) > 20:
            cleaned_paragraphs.append(cleaned)

    return cleaned_paragraphs


def extract_tables_to_dataframes(elements):
    tables = []
    for element in elements:
        if element.category == "Table":
            try:
                rows = [row.strip() for row in element.text.strip().split("\n") if row.strip()]
                table_data = [re.split(r'\s{2,}', row) for row in rows]

                if len(table_data) > 1:
                    df = pd.DataFrame(table_data[1:], columns=table_data[0])
                    tables.append(df)
            except Exception as e:
                print(f"Error parsing table: {e}")
    return tables


def process_pdf_with_langchain(pdf_path):
    # Step 1: Use LangChain loader
    loader = UnstructuredPDFLoader(pdf_path)
    docs = loader.load()

    # Step 2: Use underlying unstructured partitioner for element-level access
    elements = partition_pdf(pdf_path, extract_images_in_pdf=False)

    # Step 3: Separate paragraphs and tables
    paragraphs = extract_text_paragraphs(elements)
    tables = extract_tables_to_dataframes(elements)

    return paragraphs, tables


# def save_outputs(paragraphs, tables, txt_file="paragraphs.txt", excel_file="tables.xlsx"):
#     with open(txt_file, "w", encoding="utf-8") as f:
#         for para in paragraphs:
#             f.write(para + "\n\n")

#     with pd.ExcelWriter(excel_file) as writer:
#         for idx, df in enumerate(tables):
#             df.to_excel(writer, sheet_name=f"Table_{idx+1}", index=False)

#     print(f"Saved paragraphs to {txt_file}")
#     print(f"Saved tables to {excel_file}")


# === Run Example ===
if __name__ == "__main__":
    pdf_path = "/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/tabular_text.pdf"
    paragraphs, tables = process_pdf_with_langchain(pdf_path)

    print("\n=== Paragraphs ===")
    for i, para in enumerate(paragraphs, 1):
        print(f"\nParagraph {i}:\n{para}")
        print("-" * 80)

    print("\n=== Tables ===")
    for i, df in enumerate(tables, 1):
        print(f"\nTable {i}:\n{df.head()}")
        print("=" * 80)

    # save_outputs(paragraphs, tables)
