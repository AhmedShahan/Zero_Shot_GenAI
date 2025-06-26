from langchain.text_splitter import CharacterTextSplitter

spliter1=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=5,
    separator=" "
    
)

spliter2=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=5,
    separator=""
    
)

text="This is sample text."
result=spliter1.split_text(text)

print(result)

print(len(result))

for i in result:
    print(i)
    print("*"*10)