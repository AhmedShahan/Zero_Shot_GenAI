from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_cohere import ChatCohere
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
# model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=1.5)
model=ChatCohere(model="command-r-plus")

# Initialize the output parser
parser = StrOutputParser()

# Create the joke generation chain
joke_chain = RunnableParallel(
    joke=promptJoke | model | parser,
    level=RunnablePassthrough(),
    lines=RunnablePassthrough()
)


explanation_chain=promptExplain | model | parser



# Step 2: Create final output with joke and explanation
complete_chain = joke_chain | RunnableParallel(
    joke=lambda x: x["joke"],  # Pass the generated joke
    explanation=explanation_chain  # Use the same joke for explanation
)

# Example usage:
result = complete_chain.invoke({
    "topic": "programming", 
    "level": "beginner", 
    "lines": "3"
})
print(result)