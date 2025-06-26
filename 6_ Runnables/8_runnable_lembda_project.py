'''
Base Idea is: 
Content Generation
Calculate length of the Content using function and Runnable Lembda
if the length is more then 300 then Summarize using another LLM.
'''
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from langchain_cohere import ChatCohere
from dotenv import load_dotenv

modelGemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=1.5)

modelCohere = ChatCohere(model="command-r-plus")


MessageContent = [
    ('system', 'You are an expert AI helper for Content Generation. Please provide an Detailed Information for the given topic.'),
    ('human', 'Please provide a Detailed Information on the topic: {topic}')
]


MessageSummarize=[
    ('system','You are an Expart AI for SUmmarize in Detailedd Within 300 Words.'),
    ('human','summartize the content {content} within 300 words')
]

promptContent=ChatPromptTemplate.from_messages(MessageContent)
promptSummary= ChatPromptTemplate.from_messages(MessageSummarize)
parser=StrOutputParser()

def WordCount(content):
    return len(content.split()) > 500



ContentChain=promptContent | modelGemini | parser

branch_chain=RunnableBranch(
    (RunnableLambda(WordCount),promptSummary | modelCohere | parser),
     RunnablePassthrough()
)

chain=ContentChain | branch_chain

topic="Artificial Intelligence"

result=chain.invoke({
    "topic":topic
})

print(result)