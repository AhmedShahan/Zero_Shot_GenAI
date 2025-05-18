from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st 
from dotenv import load_dotenv
load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

st.title("Dynamic Chat Bases Summarize Bot")
input= st.text_input("Enter Your Text: ")

if st.button("Summarize"):
    response=model.invoke(input)
    st.write(response.content)