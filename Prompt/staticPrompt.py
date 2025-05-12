## First Ceate a Chat using Gemini and streamlit
'''
Paper Name (User Input)
Summarize Button
'''

from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI


from dotenv import load_dotenv
load_dotenv()


import streamlit as st
st.title("Simple Summarize Chatbot Using Open Source LLM")
st.write("This is a simple chatbot that uses Open Source LLMs to summarize text.")
input_text= st.text_input("Enter the text to summarize:")

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

if st.button("Summarize"):
    response= model.invoke(input_text)
    st.write("Google LLM Response:", response.content)

'''
problem হলও এখানে user কাছে কাছে বেশি flexibility. 
user চাইলে যেকোনো কিছু লিখতে পারে।
কিন্তু আমরা user কে এত বেশি contol দিতে চাই না।

What will be the Idea?
1) User will select a paper from the list
2) User will select explanation style from the list as: Beginer-Friendly, Code Oriented, Mathematical, Technical, Expert Level
3) User Will select the length of the explanation as: Short, Medium, Long
4) Summarize Button
'''


