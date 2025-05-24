from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda
import streamlit as st
import time

st.set_page_config(
    page_title="Your App Title",
    layout="wide",  # Use "wide" instead of "centered"
)
# App title
st.title("📝 AI BlogCraft: Dynamic Content Generator")

# Initialize session state for results and generation status
if 'outline' not in st.session_state:
    st.session_state.outline = ""
    st.session_state.expanded = ""
    st.session_state.summary = ""
    st.session_state.is_generating = False

# Available models
models = ['gemini-1.5-flash', 'command-r-plus', 'gemma3:latest', 'deepseek-r1:latest', 'llama3.2:1b']

# Model and temperature selection
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Outline Generation")
    outline_model = st.selectbox("Select Outline Model", models, key="outline_model")
    outline_temp = st.slider("Outline Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1, key="outline_temp")
with col2:
    st.subheader("Expand Generation")
    expand_model = st.selectbox("Select Expand Model", models, key="expand_model")
    expand_temp = st.slider("Expand Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1, key="expand_temp")
with col3:
    st.subheader("Summary Generation")
    summary_model = st.selectbox("Select Summary Model", models, key="summary_model")
    summary_temp = st.slider("Summary Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1, key="summary_temp")

# Topic input
topic = st.text_input("Enter Blog Topic:", placeholder="e.g., Artificial Intelligence in Healthcare")

# Generate button
generate_button = st.button("Generate Blog Content", disabled=st.session_state.is_generating)

# Mock model initializer (replace with actual API integrations if available)
class ModelInitializer(object):
    def __init__(self, model_name, temperature):
        self.model_name = model_name
        self.temperature = temperature

    def initialize(self):
        if self.model_name == 'gemini-1.5-flash':
            return ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
        elif self.model_name == 'command-r-plus':
            return ChatCohere(model="command-r-plus", temperature=0.7)
        elif self.model_name == 'gemma3:latest':
            return ChatOllama(model="gemma3:latest", temperature=1.5)
        elif self.model_name == 'deepseek-r1:latest':
            return ChatOllama(model="deepseek-r1:latest", temperature=1.5)
        elif self.model_name == 'llama3.2:1b':
            return ChatOllama(model="llama3.2:1b", temperature=0.9)
        else:
            raise ValueError("Invalid model name")

# Define the typing effect function
def stream_text(text, placeholder, delay=0.02):
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(displayed_text)
        time.sleep(delay)

# Define the LangChain pipeline
def create_pipeline(outline_model, expand_model, summary_model, outline_temp, expand_temp, summary_temp):
    # Prompts
    message_outline = [
        ('system', "You are a helpful AI Blog Outline Generator. Provide a detailed outline for a blog post on the given topic in a clear, structured format with at least 4 main sections."),
        ('human', "Generate an outline for a blog post on {topic}")
    ]
    message_expander = [
        ('system', "You are a helpful AI Blog Expander. Expand each section of the provided blog outline into a detailed paragraph (100-150 words per section). Ensure the content is engaging, informative, and relevant to the topic."),
        ('human', "Expand the following blog outline into detailed paragraphs: {outline}")
    ]
    message_summary = [
        ('system', "You are a helpful AI Blog Summarizer. Provide a concise summary of the expanded blog post in 150-200 words, capturing the key points and essence of the content."),
        ('human', "Summarize the following blog post: {blog_post}")
    ]

    # Initialize models
    model_outline = ModelInitializer(outline_model, outline_temp).initialize()
    model_expand = ModelInitializer(expand_model, expand_temp).initialize()
    model_summarize = ModelInitializer(summary_model, summary_temp).initialize()

    # Prompts
    prompt1 = ChatPromptTemplate.from_messages(message_outline)
    prompt2 = ChatPromptTemplate.from_messages(message_expander)
    prompt3 = ChatPromptTemplate.from_messages(message_summary)

    # Parser
    parser = StrOutputParser()

    # Chain
    chain = (
        prompt1
        | model_outline
        | parser
        | {"outline": RunnableLambda(lambda x: x)}
        | prompt2
        | model_expand
        | parser
        | {"blog_post": RunnableLambda(lambda x: x)}
        | prompt3
        | model_summarize
        | parser
    )
    return chain

# Handle generation
if generate_button and topic:
    st.session_state.is_generating = True
    st.session_state.outline = ""
    st.session_state.expanded = ""
    st.session_state.summary = ""

    # Create three columns for output
    col1, col2, col3 = st.columns(3)
    
    # Placeholders for loading and content
    with col1:
        st.subheader("Outline")
        outline_placeholder = st.empty()
        outline_placeholder.markdown("⏳ Generating Outline...")
    with col2:
        st.subheader("Expanded Sections")
        expand_placeholder = st.empty()
        expand_placeholder.markdown("⏳ Waiting for Outline...")
    with col3:
        st.subheader("Summary")
        summary_placeholder = st.empty()
        summary_placeholder.markdown("⏳ Waiting for Expanded Sections...")

    # Generate content
    try:
        # Step 1: Generate Outline
        outline_prompt = ChatPromptTemplate.from_messages([
            ('system', "You are a helpful AI Blog Outline Generator. Provide a detailed outline for a blog post on the given topic in a clear, structured format with at least 4 main sections."),
            ('human', "Generate an outline for a blog post on {topic}")
        ])
        outline_chain = outline_prompt | ModelInitializer(outline_model, outline_temp).initialize() | StrOutputParser()
        outline_result = outline_chain.invoke({"topic": topic})
        st.session_state.outline = outline_result
        outline_placeholder.empty()
        stream_text(outline_result, outline_placeholder)

        # Step 2: Expand Sections
        expand_placeholder.markdown("⏳ Generating Expanded Sections...")
        expand_prompt = ChatPromptTemplate.from_messages([
            ('system', "You are a helpful AI Blog Expander. Expand each section of the provided blog outline into a detailed paragraph (100-150 words per section). Ensure the content is engaging, informative, and relevant to the topic."),
            ('human', "Expand the following blog outline into detailed paragraphs: {outline}")
        ])
        expand_chain = expand_prompt | ModelInitializer(expand_model, expand_temp).initialize() | StrOutputParser()
        expand_result = expand_chain.invoke({"outline": outline_result})
        st.session_state.expanded = expand_result
        expand_placeholder.empty()
        stream_text(expand_result, expand_placeholder)

        # Step 3: Summarize
        summary_placeholder.markdown("⏳ Generating Summary...")
        summary_prompt = ChatPromptTemplate.from_messages([
            ('system', "You are a helpful AI Blog Summarizer. Provide a concise summary of the expanded blog post in 150-200 words, capturing the key points and essence of the content."),
            ('human', "Summarize the following blog post: {blog_post}")
        ])
        summary_chain = summary_prompt | ModelInitializer(summary_model, summary_temp).initialize() | StrOutputParser()
        summary_result = summary_chain.invoke({"blog_post": expand_result})
        st.session_state.summary = summary_result
        summary_placeholder.empty()
        stream_text(summary_result, summary_placeholder)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    finally:
        st.session_state.is_generating = False

# # Display cached results if available
# if st.session_state.outline or st.session_state.expanded or st.session_state.summary:
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.subheader("Outline")
#         st.markdown(st.session_state.outline)
#     with col2:
#         st.subheader("Expanded Sections")
#         st.markdown(st.session_state.expanded)
#     with col3:
#         st.subheader("Summary")
#         st.markdown(st.session_state.summary)