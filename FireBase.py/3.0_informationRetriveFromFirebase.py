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


def retrive_chat(user_id):
    # Initialize Firestore
    db = firestore.client()




authentication= authenticate_user("shahan", "123")

print(authentication[0])



