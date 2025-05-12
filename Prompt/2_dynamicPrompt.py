import streamlit as st



st.title("Basic Summarize Chatbot Using Open Source LLM")
st.write("This is a simple chatbot that uses Open Source LLMs to summarize text.")



st.selectbox("Select a Paper", ["Attention is All You Need", 
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

st.selectbox("Select Explanation Style", ["Beginer-Friendly", 
                                            "Code Oriented", 
                                            "Mathematical", 
                                            "Technical", 
                                            "Expert Level"])
st.selectbox("Select Length of Explanation", ["Short", 
                                                "Medium", 
                                                "Long"])

if st.button("Summarize"):
    st.write("Something")