from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

# Load environment variables (e.g., Google API key)
load_dotenv()

# Define the prompt templates for joke generation and explanation
MessageJoke = [
    ('system', 'You are an expert AI helper for Joke Generation. Please provide an interesting joke for the given topic.'),
    ('human', 'Please provide a joke on the topic: {topic}')
]

MessageExplanation = [
    ('system', 'You are an expert AI for explaining jokes. Please provide a clear explanation of the given joke at the specified level of detail.'),
    ('human', 'Explain the joke "{joke}" at a {level} level within {lines} lines.')
]

# Create prompt templates
promptJoke = ChatPromptTemplate.from_messages(MessageJoke)
promptExplain = ChatPromptTemplate.from_messages(MessageExplanation)

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)

# Initialize the output parser
parser = StrOutputParser()

# Create the joke generation chain
joke_chain = promptJoke | model | parser
explanation_chain=promptExplain | model | parser 

# Create the combined chain using RunnableParallel
final_chain=joke_chain | explanation_chain

# Example invocation with user inputs
user_input = {
    "topic": "Cat",
    "level": "Beginner",
    "lines": "5"
}

# Run the chain
response = final_chain.invoke(user_input)

# Print the results
print("Joke:", response["joke"])
print("Explanation:", response["explanation"])