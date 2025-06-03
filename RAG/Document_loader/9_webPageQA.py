from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
url="https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/"
loader=WebBaseLoader(url)

docs=loader.load()

MessageContent=[
    ('system','You are an Expart Assistent for Question Answer From the Given Webpage Content'),
    ('human','Please Answer the Question {question} from teh following Content {content}')
]

prompt=ChatPromptTemplate.from_messages(MessageContent)

modelGemini=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)
parser=StrOutputParser()

chain=prompt | modelGemini | parser

question="Learning in neural networks follows a structured, three-stage process"
response=chain.invoke({
    "question": question,
    "content": docs[0].page_content
})


print(response)

