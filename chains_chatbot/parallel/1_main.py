'''
############### Main Target
1) Generate a Detailed Documents using LLM and Chat Prompts
Based on this Documents We will 
            * Generate Easy Level Documents
            * A Quiz
So The user will find a Easy Level Notes and a Quiz
'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
modelGemini= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)

modelCohera=ChatCohere(model="command-r-plus")

modelLlama= ChatOllama(model="llama3.2:1b")

MessageReport=[
    ("system","You are an Advance AI for Detailed Report Generation. Give me a Detailed Report On the Given Topic."),
    ('human',"Please Provide an Detaild report On {topic}")
]


MessageNote=[
    ("system","You are an Advance AI for Note Generation in Easy Level. Give me a Easy Level and Detailed Note on the contex below"),
    ('human',"Please Provide an Detaild Note On {report}")
]

MessageQuiz=[
    ("system","You are an Advance AI for Quiz Generation. Give me 10 Question From The Notes."),
    ('human',"Please Provide 10 Questionfrom the {notes}")
]


MessageCombined=[
    ("system","You are an Advance AI for Combined.Please Combined The Below Information Carefully"),
    ('human',"Combined Notes {notes_c} and Quizes {quiz}")
]
prompt_report=ChatPromptTemplate.from_messages(MessageReport)
prompt_note=ChatPromptTemplate.from_messages(MessageNote)
prompt_quiz=ChatPromptTemplate.from_messages(MessageQuiz)
prompt_combined=ChatPromptTemplate.from_messages(MessageCombined)

parser=StrOutputParser()
report=prompt_report | modelGemini | parser

# notes= report | modelCohera | parser
# quiz= report | modelLlama| parser

parallel_chain=RunnableParallel(
    {
        "notes_c": prompt_note | modelGemini | parser,
        "quiz": prompt_quiz | modelLlama | parser

    }
)

merge_chain=prompt_combined | modelGemini | parser

chain= report | parallel_chain | merge_chain

topic="Artificial Intelligence"
response=chain.invoke(
    {"topic":topic}
)

print(response)