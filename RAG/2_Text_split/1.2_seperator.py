from langchain.text_splitter import CharacterTextSplitter

spliter1=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator="."
    
)

text="""
This is sample text1.
This is sample text2.
This is sample text3.
This is sample text4.
This is sample text5.
"""
result=spliter1.split_text(text)

print(result)

print(len(result))

for i in result:
    print(i)
    print("*"*10)