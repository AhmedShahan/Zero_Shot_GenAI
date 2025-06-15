from langchain_text_splitters import MarkdownHeaderTextSplitter
import re

text = '''

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
'''

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "header1"), ("##", "header2")])

chunks = splitter.split_text(text)

# The chunks lose the header lines, so we re-extract headers from text and prepend manually
# Extract headers with regex
headers = re.findall(r'^(#{1,2} .*)$', text, flags=re.MULTILINE)

# Now prepend header to each chunk content, assuming chunk i corresponds to header i
for i, chunk in enumerate(chunks):
    header = headers[i] if i < len(headers) else ''
    content = f"{header}\n{chunk.page_content}"
    print(f"Chunk {i}:")
    print(content)
    print("-" * 50)
