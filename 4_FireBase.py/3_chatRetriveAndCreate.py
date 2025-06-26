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
    db = firestore.client()
    try:
        user_ref = db.collection('UserChat').where('UserId', '==', user_id)
        docs = user_ref.get()
        texts = []
        for doc in docs:
            data = doc.to_dict()
            if 'text' in data:
                texts.append(data['text'])
        
        return texts

    except Exception as e:
        st.error(f"Error retrieving chat: {e}")
        return None






# Function to display the chatbot interface
def show_chatbot():
    st.title("Chatbot Interface")

    chats= retrive_chat(st.session_state.user_data['UserId'])
    print(chats)
    st.write(chats)
    

# Main app
def main():
    # Initialize session state for login status
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_data = None
    
    # Check if user is logged in
    if st.session_state.logged_in:
        # Show chatbot interface
        show_chatbot()
    else:
        # Show login page
        st.title("Chatbot Login")
        
        user_id = st.text_input("User ID", placeholder="Enter your User ID")
        user_password = st.text_input("Password", type="password", placeholder="Enter your Password")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if st.button("Login"):
                if user_id and user_password:
                    success, result = authenticate_user(user_id, user_password)
                    if success:
                        # Store user data in session state
                        st.session_state.logged_in = True
                        st.session_state.user_data = result
                        st.rerun()
                    else:
                        st.error(result)
                else:
                    st.warning("Please enter both User ID and Password")

if __name__ == "__main__":
    main()