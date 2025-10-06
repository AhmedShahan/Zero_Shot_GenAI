from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()
message=[
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
]

# Define system + history + human
prompt = ChatPromptTemplate.from_messages(message)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

chain = prompt | model

# Conversation memory
history = []

while True:
    question = input("Ask a question: ")
    if question.lower() in ["exit", "quit", "stop"]:
        print("Exiting the chatbot.")
        break

    response = chain.invoke({"input": question, "history": history})
    print("Answer:", response.content)

    # Save the conversation turn
    history.append(("human", question))
    history.append(("ai", response.content))
