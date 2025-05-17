import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("/home/shahanahmed/Zero_Shot_GenAI/Message/fir-83d69-firebase-adminsdk-fbsvc-db646197e2.json")
firebase_admin.initialize_app(cred)

# Firestore DB
db = firestore.client()


session_id = "2025_05_17_Current_time_11_15_09"  # Replace with your actual ID

doc_ref = db.collection("chat_sessions").document(session_id)
doc = doc_ref.get()

if doc.exists:
    data = doc.to_dict()
    print("Timestamp:", data.get("timestamp"))
    print("Messages:", data.get("messages"))
else:
    print("No document found with ID:", session_id)
