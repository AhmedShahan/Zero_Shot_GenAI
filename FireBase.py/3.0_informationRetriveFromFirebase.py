import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# Initialize Firebase (if not already initialized)
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate("/home/shahanahmed/Zero_Shot_GenAI/FireBase.py/learning-3b8cb-firebase-adminsdk-fbsvc-4c9eb36deb.json")
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"Firebase initialization error: {e}")

# Function to authenticate user
def authenticate_user(user_id, password):
    # Initialize Firestore
    db = firestore.client()
    
    try:
        # Query the User table for the provided credentials
        user_ref = db.collection('User').where('UserId', '==', user_id).limit(1).get()
        
        if not user_ref:
            return False, "User not found"
        
        user_data = user_ref[0].to_dict()
        
        # Check if password matches
        if user_data.get('User_password') == password:
            return True, user_data
        else:
            return False, "Incorrect password"
            
    except Exception as e:
        return False, f"Authentication error: {e}"


def retrieve_chat(user_id):
    db = firestore.client()
    try:
        user_ref = db.collection('UserChat').where('UserID', '==', user_id)  # Note: Changed 'UserId' to 'UserID' to match case
        docs = user_ref.get()
        chat_data = []
        for doc in docs:
            data = doc.to_dict()
            if 'ChatID' in data:
                chat_data.append(data['ChatID'])
        return chat_data
    except Exception as e:
        st.error(f"Error retrieving chat: {e}")
        return []




authentication= authenticate_user("ahmed", "112233")

print(authentication[0])

retrive=retrieve_chat("ahmed")
print(retrive)



