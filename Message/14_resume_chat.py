from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import ast  # To safely parse string representations of Python objects

load_dotenv()

# Define your prompt template
message = [
    ("system", "You are a helpful {domain} assistant."),
    ("human", "{input}")
]

prompt_template = ChatPromptTemplate.from_messages(message)

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

# Chat history file path
chat_history_file = "/home/shahanahmed/Zero_Shot_GenAI/Message/chat_history.txt"

# Step 1: Try to load previous chat history if available
chat_history = []
domain = "general"

if os.path.exists(chat_history_file) and os.path.getsize(chat_history_file) > 0:
    with open(chat_history_file, "r") as file:
        saved_history = file.read()
        try:
            raw_history = ast.literal_eval(saved_history)  # Converts string back to list of dict-like messages
            for msg in raw_history:
                if isinstance(msg, dict):  # Just in case
                    role = msg.get("type") or msg.get("role")  # Compatibility
                    content = msg.get("content")
                    if role == "system":
                        chat_history.append(SystemMessage(content=content))
                    elif role == "human":
                        chat_history.append(HumanMessage(content=content))
                    elif role == "ai":
                        chat_history.append(AIMessage(content=content))
        except Exception as e:
            print(f"Failed to parse previous chat history: {e}")

# Step 2: Open file for writing (truncate to overwrite later)
file = open(chat_history_file, "w")

# Step 3: Start chatbot loop
while True:
    input_query = input("Enter your query (or type 'exit' to quit): ")
    if input_query.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    elif input_query.lower() in ["domain", "change"]:
        domain = input("Enter Your Domain: ")
        input_query = input("Enter your query (or type 'exit' to quit): ")

    # Format messages using prompt
    formatted_messages = prompt_template.format_messages(domain=domain, input=input_query)

    system_message = formatted_messages[0]
    human_message = formatted_messages[1]

    chat_history.append(system_message)
    chat_history.append(human_message)

    response = model.invoke(chat_history)
    ai_message = AIMessage(content=response.content)
    chat_history.append(ai_message)

    print(f"Assistant: {ai_message.content}")

# Step 4: Save chat history
file.write(str(chat_history))
file.close()
