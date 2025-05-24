'''
Basic Sequencial Chatbot
User will ask question and bot will answer
This is a simple example of a sequential chatbot using LangChain.
'''

from  langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)
Message=[
    ('system',"You are an Helpfull AI Assistent. Please Generate Answer of the following question"),
    ('human',"{input}")
]

prompt=ChatPromptTemplate.from_messages(Message)
parser=StrOutputParser()
chain=prompt | model | parser
while True:
    question=input("Ask a question: ")
    if question.lower() in ["exit", "quit", "stop"]:
        print("Exiting the chatbot.")
        break
    response=chain.invoke({"input":question})
    print("Answer:",response)

