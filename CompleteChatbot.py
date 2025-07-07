from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st

st.set_page_config(page_title="Full Chatbot", layout="wide")
st.title("AHMED's PERSONAL CHATBOT")

# Initialize chat history only once
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0.9
)
parser = StrOutputParser()
chain = llm | parser

# Get user input
input_query = st.chat_input("Enter Your query")
if input_query:
    # Show user message
    with st.chat_message("user"):
        st.write(input_query)

    # Append user message to chat history
    st.session_state.chat_history.append(HumanMessage(input_query))

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke(st.session_state.chat_history)
            st.write(response)

    # Append bot response to chat history
    st.session_state.chat_history.append(AIMessage(response))

# Optionally, show full chat history on page load:
for message in st.session_state.chat_history:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(message.content)
