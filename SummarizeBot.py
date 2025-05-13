## Simpel Summarize Chatbot Using Opensource/free LLM and ChatLLM using streamlit

from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere

import streamlit as st

model1= GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
model2= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
model3= ChatCohere(model="command-r-plus")


st.title("Simple Summarize Chatbot Using Open Source LLM")
st.write("This is a simple chatbot that uses Open Source LLMs to summarize text.")

input_text= st.text_input("Enter the text to summarize:")

# Initialize session state variables
# Initialize session state variables
if "result1" not in st.session_state:
    st.session_state.result1 = None
    st.session_state.result2 = None
    st.session_state.result3 = None

# Text input
# input_text = st.text_area("Enter text to summarize:")

# First button to generate summaries
if st.button("Summarize"):
    st.session_state.result1 = model1.invoke(input_text)
    st.session_state.result2 = model2.invoke(input_text)
    st.session_state.result3 = model3.invoke(input_text)

# Show buttons in bat (horizontal) format if any results exist
if any([st.session_state.result1, st.session_state.result2, st.session_state.result3]):
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Summarize from Google"):
            st.write("Google LLM Response:", st.session_state.result1)

    with col2:
        if st.button("Summarize from ChatGoogle"):
            st.write("ChatGoogle LLM Response:", st.session_state.result2.content)

    with col3:
        if st.button("Summarize from Cohere"):
            st.write("Cohere Response:", st.session_state.result3.content)

elif not any([st.session_state.result1, st.session_state.result2, st.session_state.result3]):
    st.write("No results available yet.")