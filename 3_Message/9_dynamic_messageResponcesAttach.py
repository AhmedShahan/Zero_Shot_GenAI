from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# Define the message template
Message = [
    ('system', "You are a helpful {domain} assistant."),
    ('human', "{input}"),
]

# Create a ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(Message)

# Set your variables
domain = "Mathematics"
input_query = "What is PI"

# To see the initialized prompt with variables filled in
formatted_prompt = prompt.invoke({"domain": domain, "input": input_query})
print(formatted_prompt)

