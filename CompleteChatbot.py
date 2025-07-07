from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm=ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0.9
)
parser=StrOutputParser()
chain= llm| parser

while True:
    input_query=input("Enter your Query: ")
    if input_query.lower() in ['quite','exit']:
        print("Exiciting Chatbot. Good Bye")
        break
    else:
        response=chain.invoke(input_query)
        print(response)