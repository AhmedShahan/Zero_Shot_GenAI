from langchain.text_splitter import MarkdownHeaderTextSplitter

# The Markdown text you want to split.
text='''
# My Markdown Document

## Introduction

This is a **simple** Markdown document.  
Markdown allows you to write using an easy-to-read, easy-to-write plain text format.

## Features

- Easy to use
- Lightweight syntax
- Converts to HTML

## Code Example

Here’s a Python code snippet:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```
'''

# Define the headers to split on.
# In this case, we are splitting on level 1 (#) and level 2 (##) headings.
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

# Create the splitter instance, keeping the headers in the content.
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on, strip_headers=False
)

# Split the text. The output is a list of Document objects.
chunks = markdown_splitter.split_text(text)

# Print each chunk's content and metadata.
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print("Content:")
    print(chunk.page_content)
    # print("\nMetadata:")
    # print(chunk.metadata)
    print("*"*50)