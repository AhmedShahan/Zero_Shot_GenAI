import streamlit as st
from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt



st.title("Basic Summarize Chatbot Using Open Source LLM")
st.write("This is a simple chatbot that uses Open Source LLMs to summarize text.")



paper_title=st.selectbox("Select a Paper", ["Attention is All You Need", 
                                "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", 
                                "Language Models are Unsupervised Multitask Learners",
                                "Scaling Laws for Neural Language Models",
                                "Training Language Models to Follow Instructions with Human Feedback",
                                "T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer",
                                "XLNet: Generalized Autoregressive Pretraining for Language Understanding",
                                "RoBERTa: A Robustly Optimized BERT Pretraining Approach",
                                "ALBERT: A Lite BERT for Self-supervised Learning of Language Representations",
                                "DistilBERT: A Distilled Version of BERT: Smaller, Faster, Cheaper, and Lighter",
                                "ERNIE: Enhanced Representation through kNowledge Integration",
                                ])

explanation_style= st.selectbox("Select Explanation Style", ["Beginer-Friendly", 
                                            "Code Oriented", 
                                            "Mathematical", 
                                            "Technical", 
                                            "Expert Level"])
explanation_length= st.selectbox("Select Length of Explanation", ["Short", 
                                                "Medium", 
                                                "Long"])





Research_prompt=load_prompt("/home/shahanahmed/Zero_Shot_GenAI/template.json")



model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

if st.button("Summarize"):
    chain=Research_prompt | model
    result=chain.invoke({
        "paper_title":paper_title,
        "explanation_style": explanation_style,
        "explanation_length": explanation_length
    })
    st.write("Generating summary...")
        # First, format the prompt with the user's selections
    st.write("Google LLM Response:", result.content)
