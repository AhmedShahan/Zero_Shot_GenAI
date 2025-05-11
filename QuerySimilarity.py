## Based on the Embedding, We will extract The document and show the similarity


## Let say We have some documents of 5 Different Person in a document list

documents=[
    "Shakib Al Hasan is a world-class all-rounder, excelling in left-arm spin and aggressive batting, consistently ranked among the top all-rounders globally. He holds records like Bangladesh’s highest ODI wicket-taker.",
    "Tamim Iqbal, Bangladesh’s top run-scorer, is known for his elegant left-handed batting. He scored the nation’s first Test double century.",
    "Mushfiqur Rahim, a gritty wicketkeeper-batsman, has been crucial in many victories. He was the first Bangladeshi to score a Test double century.",
    "Mahmudullah Riyad, a versatile middle-order batsman and off-spinner, shines in clutch T20 and ODI moments. He has captained Bangladesh with composure.",
    "Mustafizur Rahman, a left-arm pacer, is famed for his deceptive cutters, dominating limited-overs cricket. His unique style earned IPL stardom.",
]


## Now First Embedding
from langchain_huggingface import HuggingFaceEmbeddings


embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
DocumentEmbed=embedding.embed_documents(documents)

Query="Tell Me about left-arm pacer"

QueryEmbed=embedding.embed_query(text=Query)

# print("Document Embedding")
# print(DocumentEmbed)


# print("Query Embedding")
# print(QueryEmbed)

##### Checking the Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity



### cosine similarity(x,y)
# x= query embedding in 2D Array, already Embedding korar somoy 1D list e ache
# y= Document Embedding, Already 2D array tei ache. 

score=cosine_similarity([QueryEmbed],DocumentEmbed)
# print(score)

'''
Returns 2D So make it 1D
'''
score1D=score[0]
# print(score1D)
# print(type(score1D))

### এবার আমরা চাচ্ছি সবচেয়ে কম স্কোর এর information দেখতে। তাহলে প্রথএম সর্ট কওরা লাগবে। তার আগে আমরা প্রতিটা score এর corrosponding index number dei. 

indexed_score=list(enumerate(score1D))

print("Indexed: ",indexed_score)

sorted_Score_index = sorted(indexed_score, key=lambda x: x[1])

# print("Sorted Array\n",sorted_Score_index = sorted(indexed_score, key=lambda x: x[1]))


## Now it is sorted with indexed in lower to Higher.
## We want the maximum highest Score with Index. 

h_index, h_score=sorted_Score_index[-1]

print("Highest Score: ",h_score)
print("Highest Index: ", h_index)

print("Relevent Document:\n",documents[int(h_index)])





