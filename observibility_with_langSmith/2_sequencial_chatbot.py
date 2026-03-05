from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
## llm config
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

prompt_report=[
    ("system","You are an Expart AI for generating Report"),
    ("human","Please write down a Detailed report on tipic {topic}")
]

prompt_summary=[
    ("system","You are an Expart AI for generating Summary"),
    ("human","Please write down a 100 words summary on Report {report}")
]

from langchain_core.prompts import ChatPromptTemplate

prompt_report=ChatPromptTemplate.from_messages(prompt_report)
prompt_summary=ChatPromptTemplate.from_messages(prompt_summary)

from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()

chain=prompt_report | llm | parser | prompt_summary | llm | parser

input_text="Artificial Intelligence"
response=chain.invoke({
    "topic":input_text
})

print(response)