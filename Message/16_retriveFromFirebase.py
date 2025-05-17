import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("/home/shahanahmed/Zero_Shot_GenAI/Message/fir-83d69-firebase-adminsdk-fbsvc-db646197e2.json")
firebase_admin.initialize_app(cred)
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Firestore DB
db = firestore.client()


session_id = "2025_05_17_Current_time_11_56_36"  # Replace with your actual ID

doc_ref = db.collection("chat_sessions").document(session_id)
doc = doc_ref.get()

# if doc.exists:
#     data = doc.to_dict()
#     print("Timestamp:", data.get("timestamp"))
#     print("Messages:", data.get("messages"))
# else:
#     print("No document found with ID:", session_id)

import os

chat_history = []
import re
if doc.exists:
    data = doc.to_dict()
    try:
        messages = data.get("messages", [])
        for item in messages:
            if item["type"] == "SystemMessage":
                chat_history.append(SystemMessage(content=item["content"]))
            elif item["type"] == "HumanMessage":
                chat_history.append(HumanMessage(content=item["content"]))
            elif item["type"] == "AIMessage":
                chat_history.append(AIMessage(content=item["content"]))
    except Exception as e:
        print("Failed to load chat history:", e)

print(chat_history)
# Define prompt template
message = [
    ("system", "You are a helpful {domain} assistant."),
    ("human", "{input}")
]
prompt_template = ChatPromptTemplate.from_messages(message)

# Default domain
domain = "general"

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

from datetime import datetime
chat_data = [{"type": msg.__class__.__name__, "content": msg.content} for msg in chat_history]
session_id = datetime.now().strftime("%Y_%m_%d_Current_time_%H_%M_%S")  # e.g., 2025_05_17_Current_time_15_47_22

db.collection("chat_sessions").document(session_id).set({
    "messages": chat_data
})