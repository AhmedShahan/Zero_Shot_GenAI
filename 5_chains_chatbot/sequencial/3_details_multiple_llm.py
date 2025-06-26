'''
🔧 Idea: "Automated Blog Post Generator from a Topic"
This app will:

Take a topic input from the user.

Generate an outline of the blog.

Expand each outline point into a detailed paragraph.

Summarize the blog post at the end.

You can chain multiple LLMs (or just reuse one) to perform these tasks in sequence.


          [User Input]
               │
               ▼
   ┌───────────────────────────┐
   │ Step 1: Generate Outline  │ ← (LLM 1)
   └───────────────────────────┘
               │
               ▼
   ┌───────────────────────────┐
   │ Step 2: Expand Sections   │ ← (LLM 2)
   └───────────────────────────┘
               │
               ▼
   ┌───────────────────────────┐
   │ Step 3: Summarize Blog    │ ← (LLM 3)
   └───────────────────────────┘
               │
               ▼
         [Final Output]
'''


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from langchain_ollama import ChatOllama

load_dotenv()
model1 = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

model2 = ChatCohere(
    model="command-r-plus",
    temperature=0.9
)

model3= ChatOllama(
    model="gemma3:latest",
    temperature=1.5

)


Message_outline=[
    ('system',"You are a helpful AI Blog Outline Generator. Please Provide a Detailed outline of the following topic"),
    ('human',"Generate an outline for a blog post on {topic}")
]
Message_section=[
    ('system', "You are a helpful AI Blog Section Expander. Please Provide a Detailed, accurate and brief section of the following outline"),
    ('human', "Expand the outline point {outline_point} into a detailed paragraph")
]

Message_Expender=[
    ('system', "You are a helpful AI Blog Expander. Please Provide a Detailed, accurate and brief summary of the following blog post"),
    ('human', "Summarize the blog post: {blog_post} in 10 lines")
]

Message_summary=[
    ('system', "You are a helpful AI Blog Summarizer. Please Provide a Detailed, accurate and brief summary of the following blog post"),
    ('human', "Summarize the blog post: {blog_post} in 20 lines")
]


prompt1=ChatPromptTemplate.from_messages(Message_outline)
prompt2=ChatPromptTemplate.from_messages(Message_section)
prompt3=ChatPromptTemplate.from_messages(Message_Expender)
prompt4=ChatPromptTemplate.from_messages(Message_summary)

parser=StrOutputParser()


topic="Artificial Intelligence in Healthcare"

chain=prompt1 | model1 | parser | prompt2 | model2 | parser | prompt3 | model3 | parser | prompt4 | model1 | parser

chain.get_graph().print_ascii()
result = chain.invoke({"topic": topic})
print("Blog Post:", result)
