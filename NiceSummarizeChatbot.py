import streamlit as st
from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere

# Initialize models
model1 = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
model2 = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
model3 = ChatCohere(model="command-r-plus")

# Streamlit page setup
st.set_page_config(page_title="Summarizer Bot", page_icon="📝")
st.title("📝 Chat Summarizer Bot")
st.markdown("💬 Talk to the bot and **switch between model responses** easily.")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_summaries" not in st.session_state:
    st.session_state.last_summaries = {}

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg["avatar"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type something to summarize...")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input, "avatar": "🧑‍💻"})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Summarizing using all models..."):
            g_response = model1.invoke(user_input)
            chatg_response = model2.invoke(user_input)
            cohere_response = model3.invoke(user_input)

            # Save summaries
            st.session_state.last_summaries = {
                "Google Gemini": g_response,
                "ChatGoogle Gemini": chatg_response.content,
                "Cohere": cohere_response.content
            }

        # Display tabs to switch responses
        tab1, tab2, tab3 = st.tabs(["🔹 Google Gemini", "🔹 ChatGoogle Gemini", "🔹 Cohere"])

        with tab1:
            st.markdown(f"**Google Gemini Response:**\n\n{g_response}")

        with tab2:
            st.markdown(f"**ChatGoogle Gemini Response:**\n\n{chatg_response.content}")

        with tab3:
            st.markdown(f"**Cohere Response:**\n\n{cohere_response.content}")

        # Save a combined summary in chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": "✅ Responses generated. Use the tabs above to view each model's summary.",
            "avatar": "🤖"
        })
