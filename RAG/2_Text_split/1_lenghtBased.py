from langchain.text_splitter import CharacterTextSplitter

spliter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=" "
    
)

text="""
The NovaX Pro 12 is an absolute powerhouse in a sleek design. The 120Hz AMOLED display is stunning, 
making everything from streaming to scrolling buttery smooth. The camera system is top-tier, especially the night mode, 
which rivals professional DSLR results. Battery life easily lasts more than a day, and the fast charging is a 
game-changer — 0 to 80% in just 30 minutes! The UI is clean, responsive, and free from bloatware. 
Overall, it's a flagship experience at a competitive price.
"""
result=spliter.split_text(text)

print(result)

print(len(result))

for i in result:
    print(i)