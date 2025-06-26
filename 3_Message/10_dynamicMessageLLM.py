from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Define the message template
Message = [
    ('system', "You are a helpful {domain} assistant."),
    ('human', "{input}"),
]


from langchain_google_genai import ChatGoogleGenerativeAI

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=1.5)


# Create a ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(Message)

# Set your variables
domain = "Mathematics"
input_query = "What is PI"

chain= prompt | model
response=chain.invoke({"domain": domain, "input": input_query})
print(response.content)

