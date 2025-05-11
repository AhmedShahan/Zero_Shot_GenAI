## Based on the Embedding, We will extract The document and show the similarity


## Let say We have some documents of 5 Different Person in a document list

documents=[
    "Shakib Al Hasan is a world-class all-rounder, excelling in left-arm spin and aggressive batting, consistently ranked among the top all-rounders globally. He holds records like Bangladesh’s highest ODI wicket-taker."
    "Tamim Iqbal, Bangladesh’s top run-scorer, is known for his elegant left-handed batting. He scored the nation’s first Test double century."
    "Mushfiqur Rahim, a gritty wicketkeeper-batsman, has been crucial in many victories. He was the first Bangladeshi to score a Test double century."
    "Mahmudullah Riyad, a versatile middle-order batsman and off-spinner, shines in clutch T20 and ODI moments. He has captained Bangladesh with composure."
    "Mustafizur Rahman, a left-arm pacer, is famed for his deceptive cutters, dominating limited-overs cricket. His unique style earned IPL stardom."
]


## Now First Embedding
from langchain_huggingface import HuggingFaceEmbeddings


embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
DocumentEmbed=embedding.embed_documents(documents)

Query="Tell Me about Sakib Al Hasan"

QueryEmbed=embedding.embed_query(text=Query)

print("Document Embedding")
print(DocumentEmbed)


print("Query Embedding")
print(QueryEmbed)