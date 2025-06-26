'''
load the txt file and summarize using LLM
'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

MessageSummary=[
    ('system','You are an Expart Assistent for Summary Generation'),
    ('human','Please Summarize the provided content {content}')
]

prompt=ChatPromptTemplate.from_messages(MessageSummary)

modelGemini=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)
parser=StrOutputParser()
from langchain_community.document_loaders import TextLoader
loader=TextLoader('/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/text.txt')

docs=loader.load()

chain=prompt | modelGemini | parser

response=chain.invoke({
    "content":docs[0].page_content
})

print(response)