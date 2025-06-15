from langchain_google_genai  import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


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

'''



from langchain_text_splitters import RecursiveCharacterTextSplitter


from langchain.text_splitter import Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0
)

chunk=splitter.split_text(text)
print(chunk)
