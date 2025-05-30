from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
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

# Create a function to prepare explanation input
def prepare_explanation_input(inputs):
    return {
        "joke": inputs["joke"],
        "level": inputs["level"], 
        "lines": inputs["lines"]
    }

# Create the explanation chain
explanation_chain = RunnableLambda(prepare_explanation_input) | promptExplain | model | parser

# Create the complete chain that generates joke and then explains it
complete_chain = RunnableParallel(
    joke=joke_chain,
    explanation=RunnableParallel(
        joke=joke_chain,
        level=RunnablePassthrough(),
        lines=RunnablePassthrough()
    ) | explanation_chain
)

# Example usage:
result = complete_chain.invoke({
    "topic": "programming", 
    "level": "beginner", 
    "lines": "3"
})

print(result)
# 

# Output will be:
# {
#     "joke": "Generated joke here...",
#     "explanation": "Explanation of the joke here..."
# }