from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st

st.set_page_config(page_title="Full Chatbot",layout="wide")
st.title("AHMED's PERSONAL CHATBOT")

llm=ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0.9
)
parser=StrOutputParser()
chain= llm| parser
chat_history=[]

input_query=st.chat_input("Enter Your query")
if input_query:
    # Show user's message
    with st.chat_message("user"):
        st.write(input_query)
    chat_history.append(HumanMessage(input_query))
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response=chain.invoke(chat_history)
            st.write(response)
            chat_history.append(AIMessage(response))