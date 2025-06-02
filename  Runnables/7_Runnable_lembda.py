'''
Main Target is: 
Generate Content with totasl number of word. 
Content Generate : LLM
Word Count: python function
'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_cohere import ChatCohere
from dotenv import load_dotenv

# Load environment variables (e.g., Google API key)
load_dotenv()

MessageContent = [
    ('system', 'You are an expert AI helper for Content Generation. Please provide an Detailed Information for the given topic.'),
    ('human', 'Please provide a Detailed Information on the topic: {topic}')
]

promptContent=ChatPromptTemplate.from_messages(MessageContent)
parser = StrOutputParser()

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=1.5)
chainJoke=promptContent | model | parser

topic="Artificial Intelligent"



def wordCount(content):
    return len(content.split())



# result2=runnable_wordCount.invoke("What is the Name of Bangladesh?")
# print(result2)


parallel_chain=RunnableParallel(
    {"content": RunnablePassthrough(),
     "words": RunnableLambda(wordCount)
    }
)

chain=chainJoke | parallel_chain 

result=chain.invoke({
    "topic": topic
})

print(result)