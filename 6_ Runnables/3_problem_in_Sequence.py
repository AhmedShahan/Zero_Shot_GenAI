'''
Generate a Joke
Explain the joke
'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()


MessageJoke=[
    ('system','You are an Helpful Assistent for Joke Generation. Please Provike a Joke on teh Given Topic'),
    ('human','Provide A joke on topic {topic}')
]

Message_explainJoke=[
    ('system',"You are an Helpful Assistant for Explaining Joke. Please providde a Detailed Accurate Explain of the Folloing Joke"),
    ('human','Provide the Explanation of the Joke {joke}')
]

promptJoke=ChatPromptTemplate.from_messages(MessageJoke)

promptExplanation=ChatPromptTemplate.from_messages(Message_explainJoke)


model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)

parser=StrOutputParser()
chain= RunnableSequence(promptJoke,model,parser,promptExplanation,model,parser)

joke="Cat"
response=chain.invoke(
    {
        "topic":joke
    }
)

print(response)

'''
This is a simple pun, playing on two meanings of the word "mouse."

* **Meaning 1:** A small rodent, often a pest in homes and offices.  This is the traditional meaning and the one we associate with cats hunting them.

* **Meaning 2:** A computer input device.  This is the meaning relevant to the computer context in the joke.

The humor comes from the unexpected juxtaposition of these two meanings.  The setup ("Why was the cat sitting on the computer?") leads us to expect a reason related to computer activity, perhaps the cat accidentally knocked something over, or is using the computer in some absurd way.  Instead, the punchline uses the cat's predatory instinct, applying it to the computer mouse, creating a funny and slightly absurd image.  The cat isn't using the computer; it's hunting what it *thinks* is a mouse.

'''


######## ITS just Show The Explanation Because Sequencial Chain Only Shows the last output Parse. 
# How Can we Print The Joke and also The explanation
## So we need Parallel chain also Runnable Passthrough

