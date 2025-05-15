import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def initialize_firebase():
        try:
            cred = credentials.Certificate("/home/shahanahmed/Zero_Shot_GenAI/FireBase.py/learning-3b8cb-firebase-adminsdk-fbsvc-4c9eb36deb.json")
            firebase_admin.initialize_app(cred)
            return True
        except Exception as e:
            st.error(f"Failed to initialize Firebase: {e}")
            return False


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

# Main app
def main():
    st.title("Chatbot Login")
    
    # Create session state for login status if it doesn't exist
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        with st.form("login_form"):
            user_id = st.text_input("User ID", placeholder="Enter your User ID")
            user_password = st.text_input("Password", type="password", placeholder="Enter your Password")
            
            submit_button = st.form_submit_button("Login")
            
            if submit_button:
                if user_id and user_password:
                    # Initialize Firebase if not already initialized
                    if initialize_firebase():
                        success, result = authenticate_user(user_id, user_password)
                        
                        if success:
                            st.session_state.logged_in = True
                            st.session_state.user_data = result
                            st.success("Login successful!")
                            # st.experimental_rerun()
                        else:
                            st.error(result)
                    else:
                        st.error("Firebase initialization failed. Check your configuration.")
                else:
                    st.warning("Please enter both User ID and Password")
    else:
        # User is logged in, show the main application
        st.success(f"Welcome, {st.session_state.user_data.get('User_id', 'User')}!")
        
        # Add your main application content here
        st.write("Your chatbot application goes here")
        
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_data = None
            # st.experimental_rerun()

if __name__ == "__main__":
    main()