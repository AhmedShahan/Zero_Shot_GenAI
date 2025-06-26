######### Chat History Store into Firebase

'''
- Go to Firebase: https://firebase.google.com/
- Go to Firebase COnsol: https://console.firebase.google.com/u/0/?pli=1 (After created account)
- Create A Firebase Project
- Enter Your Project Name
- 

'''

import firebase_admin
from firebase_admin import credentials, firestore

# Load credentials
cred = credentials.Certificate("/home/shahanahmed/Zero_Shot_GenAI/Message/fir-83d69-firebase-adminsdk-fbsvc-db646197e2.json")
firebase_admin.initialize_app(cred)

# Firestore DB
db = firestore.client()


from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

messages=[
    SystemMessage(content="You are a helpful assistant."),
]

model= GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
while True:
    user_input= input("You: ")
    messages.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response= model.invoke(messages)
    messages.append(AIMessage(content=response))
    print(f"AI: {response}")

import datetime

serialized_messages = [msg.dict() for msg in messages]
db.collection("chat_sessions").add({
    "timestamp": datetime.datetime.now().isoformat(),
    "messages": serialized_messages
})





