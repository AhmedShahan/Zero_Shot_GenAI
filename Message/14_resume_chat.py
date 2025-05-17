from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import ast
import os

load_dotenv()

# Restore chat history if file exists
chat_history_path = "/home/shahanahmed/Zero_Shot_GenAI/Message/chat_history.txt"
chat_history = []
import re
if os.path.exists(chat_history_path):
    with open(chat_history_path, "r") as f:
        data = f.read()

    # Match strings like SystemMessage(content='...') and extract type and content
    pattern = r"(SystemMessage|HumanMessage|AIMessage)\(content='(.*?)'(?:,.*?)?\)"
    matches = re.findall(pattern, data)

    for msg_type, content in matches:
        # Unescape any escaped single quotes
        content = content.replace("\\'", "'")
        if msg_type == "SystemMessage":
            chat_history.append(SystemMessage(content=content))
        elif msg_type == "HumanMessage":
            chat_history.append(HumanMessage(content=content))
        elif msg_type == "AIMessage":
            chat_history.append(AIMessage(content=content))

# Define prompt template
message = [
    ("system", "You are a helpful {domain} assistant."),
    ("human", "{input}")
]
prompt_template = ChatPromptTemplate.from_messages(message)

# Default domain
domain = "general"

# Initialize file for writing chat history
file = open(chat_history_path, "w")

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

# Start chatbot loop
while True:
    input_query = input("Enter your query (or type 'exit' to quit): ")
    if input_query.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    elif input_query.lower() in ['domain', 'change']:
        domain = input("Enter Your Domain: ")
        input_query = input("Enter your query (or type 'exit' to quit): ")

    # Format messages using the prompt template
    formatted_messages = prompt_template.format_messages(domain=domain, input=input_query)

    # Extract and add system and human messages
    system_message = formatted_messages[0]
    human_message = formatted_messages[1]

    chat_history.append(system_message)
    chat_history.append(human_message)

    # Invoke model
    response = model.invoke(chat_history)

    # Add AI response to history
    ai_message = AIMessage(content=response.content)
    chat_history.append(ai_message)

    # Display response
    print(f"Assistant: {ai_message.content}")

# Save chat history before exit
file.write(str(chat_history))
file.close()
