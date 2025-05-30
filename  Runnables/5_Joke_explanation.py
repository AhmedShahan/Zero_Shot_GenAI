from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
load_dotenv()

MessageJoke=[
    ('system','You are an Expart AI helper for Joke Generation. Please Provide an Interasting Joke for the given topic'),
    ('human','Please provvide a Joke in given {topic}')
]


MessageExplanation=[
    ('system','you are an Expart AI for Explaning Joke. Please Provide all the possible Explanation of the Joke'),
    ('human','explain the provided Joke {joke}')
]

promptJoke=ChatPromptTemplate.from_messages(MessageJoke)
promptExplain=ChatPromptTemplate.from_messages(MessageExplanation)


model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)
parser=StrOutputParser()
runnable=RunnablePassthrough()
joke=promptJoke | model | parser

chain=RunnableParallel(
    {
        "joke":runnable.invoke(joke),
        "explanation":promptExplain | model | parser
    }
)

topic="Cat"

final_chain=joke | chain

response=final_chain.invoke({
    "topic":topic
})


print(response["joke"])
print(response["explanation"])



