import streamlit as st
from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate



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


simple_templet="""
Please summarize the research paper titled '{paper_title}' with the following specification: 
Explain Style: {explanation_style}
Explanation Lenght: {explanation_length}
1. Mathematical Details: 
    - Include relevent Mathematical equations if present in paper. 
    - Explain the mathematical concept using simple, intutive code snippet where applicable. 

2. Technical Details:
    - Include relevent technical details if present in paper. 
    - Explain the technical concept using simple, intutive code snippet where applicable.

3. Code Oriented:
    - Include relevent code snippets if present in paper. 
    - Explain the code using simple, intutive code snippet where applicable.

4. Analogical: 
    - Use relevant analogies to simplify complex concepts or ideas.    
If certain information is not in the paper, respond with "Information not available in the paper" instead of guessing or making assumptions.
Ensure that the summary is clear, concise, and easy to understand for someone who may not be familiar with the topic.
"""




prompt=PromptTemplate(
    input_variables=["paper_title", "explanation_style", "explanation_length"],
    template=simple_templet,
    validate_template=True,
)

## Fill the placeholder in the template with the user input
# prompt.invoke(
#     {
#         'paper_title': paper_title,
#         'explanation_style': explanation_style,
#         'explanation_length': explanation_length,
#     }
# )


model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

if st.button("Summarize"):
    st.write("Generating summary...")
        # First, format the prompt with the user's selections
    formatted_prompt = prompt.format(
        paper_title=paper_title,
        explanation_style=explanation_style,
        explanation_length=explanation_length
    )
    result= model.invoke(formatted_prompt)
    st.write("Google LLM Response:", result.content)
