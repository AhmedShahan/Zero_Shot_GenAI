from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Define the message template
Message = [
    ('system', "You are a helpful {domain} assistant."),
    ('human', "{input}"),
]

chat_history = []
from langchain_google_genai import ChatGoogleGenerativeAI

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=1.5)


# Create a ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(Message)

domain=input("Enter the domain: ")
while True:
    input_query = input("Enter your query (or type 'exit' to quit): ")
    if input_query.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    chain= prompt | model
    chain.invoke({"domain": domain, "input": input_query})
    response=chain.invoke({"domain": domain, "input": input_query})
    chat_history.append({"domain": domain, "input": input_query, "response": response.content})
    print(response.content)
print("Chat History:", chat_history)
