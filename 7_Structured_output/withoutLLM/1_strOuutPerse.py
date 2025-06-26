from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)


### Without StrOutputParser
response=model.invoke("What is the Capital of Bangladesh?")

print(response.content)

## with output parser

parser=StrOutputParser()
chain=model | parser
response=chain.invoke("What is the Capital of Bangladesh?")
print(response)