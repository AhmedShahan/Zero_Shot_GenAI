from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st 
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

st.title("Dynamic Chat Based Summarize Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Welcome to the Paper Summarizer Bot. Please provide the title of the paper you want to summarize."}
    ]
    st.session_state.paper_title = None
    st.session_state.awaiting_title = True

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type something...")

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
        
    # Process based on current state
    if st.session_state.awaiting_title:
        # User is providing paper title
        if len(user_input) > 5:  # Basic validation
            st.session_state.paper_title = user_input
            st.session_state.awaiting_title = False
            
            # Confirmation message
            response = f"Thank you! I'll use '{user_input}' as the paper title. Now please enter the text you want to summarize."
        else:
            response = "That doesn't seem like a valid paper title. Please provide a title with at least 5 characters."
    else:
        # User is providing text to summarize
        prompt = f"Summarize the following text from the paper titled '{st.session_state.paper_title}':\n\n{user_input}"
        llm_response = model.invoke(prompt)
        response = llm_response.content
        
        # Reset for next paper
        st.session_state.awaiting_title = True
        st.session_state.paper_title = None
        response += "\n\nWould you like to summarize another paper? If so, please provide the new paper title."
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)