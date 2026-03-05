from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
## llm config
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

prompt_message=[
    ("system","You are an Expart AI for Answer the Question"),
    ("human","Please Give the Answwer of the following Question {question}")
]

from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages(prompt_message)

from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()

chain=prompt | llm | parser

input_text="What is Machine Intelligence"
response=chain.invoke({
    "question":input_text
})

print(response)