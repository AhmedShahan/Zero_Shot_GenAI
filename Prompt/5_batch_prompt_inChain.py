from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.)

query="What is AI"


MessageExplain=[
    ('system','You are an Expart System for Explanation. Please Explain the topic in breaf manner.'),
    ('human','Please Explain the topic {topic}')
]
prompt=ChatPromptTemplate.from_messages(MessageExplain)

chain=prompt | model


# query="Artificial Intelligence"
# Step 4: Batch of inputs
multipleQueries = [
    {"topic": "Artificial Intelligence"},
    {"topic": "Block Chain"},
    {"topic": "Agentic AI"},
]

# Step 5: Call batch
responses = chain.batch(multipleQueries)

# Step 6: Print results
for i, r in enumerate(responses):
    print(f"Response {i+1}:\n{r.content}\n")