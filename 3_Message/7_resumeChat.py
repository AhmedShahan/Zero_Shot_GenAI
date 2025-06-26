import firebase_admin
from firebase_admin import credentials, firestore
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import datetime

# Initialize Firebase
cred = credentials.Certificate("/home/shahanahmed/Zero_Shot_GenAI/Message/fir-83d69-firebase-adminsdk-fbsvc-db646197e2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Load environment variables
load_dotenv()

# Load the most recent chat session from Firebase
chat_sessions = db.collection("chat_sessions").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1).stream()
messages = []

for session in chat_sessions:
    data = session.to_dict()
    for msg in data["messages"]:
        msg_type = msg["type"]
        content = msg["content"]
        if msg_type == "human":
            messages.append(HumanMessage(content=content))
        elif msg_type == "ai":
            messages.append(AIMessage(content=content))
        elif msg_type == "system":
            messages.append(SystemMessage(content=content))

# Re-initialize the model
model = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    messages.append(HumanMessage(content=user_input))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response))
    print(f"AI: {response}")

# Save the updated conversation
serialized_messages = [msg.dict() for msg in messages]
db.collection("chat_sessions").add({
    "timestamp": datetime.datetime.now().isoformat(),
    "messages": serialized_messages
})
