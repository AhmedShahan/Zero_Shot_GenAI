'''
from teh csv file, Generate a Texual Content. Means a single paragraph
'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

MessageContent=[
    ('system','You are an Expart Assistent for Content Generation'),
    ('human','Please Paragraph wise Content from the provided content {content}')
]

prompt=ChatPromptTemplate.from_messages(MessageContent)

modelGemini=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)
parser=StrOutputParser()
from langchain_community.document_loaders import CSVLoader
loader=CSVLoader('/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/bdeconomy.csv')

docs=loader.load()

contents=[]
for i in range(len(docs)):
    content=docs[i].page_content
    contents.append(content)

chain=prompt | modelGemini | parser



response=chain.invoke({
    "content":contents
})

print(response)