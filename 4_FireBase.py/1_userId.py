import streamlit as st


user_id=["shahan", "ahmed", "shahanahmed"]
user_password=["123", "456", "789"]

st.title("Chatbot Login")
user_id=st.text_input("User ID", placeholder="Enter your User ID")
user_password=st.text_input("Password", type="password", placeholder="Enter your Password")
if st.button("Login"):
    if user_id and user_password:
        st.success("Login successful!")
