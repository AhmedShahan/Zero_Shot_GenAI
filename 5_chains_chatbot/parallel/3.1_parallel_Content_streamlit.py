from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# Page setup
st.set_page_config(page_title="AI BlogCraft", layout="wide")
st.title("Parallel Content Generation with Multiple LLMs")

# Input
input_topic = st.text_input("Enter the topic for content generation:", "বাংলাদেশের ইতিহাস ও সংস্কৃতি")

# Initialize models
modelGemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)
modelCohere_r_plus = ChatCohere(model="command-r-plus", temperature=0.9)
modelCohere_r = ChatCohere(model="command-r", temperature=0.9)

# Prompts
Message_Content = [
    ('system', "You are an AI Assistant for Content Generation. Please generate a detailed, unique, engaging, and easy-to-understand content in Bangla."),
    ('human', "Generate content for the topic {topic} in Bangla Native Language")
]

MessageAddition = [
    ('system', "You are an advanced AI for content aggregation. Please merge all contents logically and sequentially. Respond in Bangla."),
    ('human', "Aggregate the content as follows: {content1}, {content2}, {content3}")
]

prompt_content = ChatPromptTemplate.from_messages(Message_Content)
prompt_addition = ChatPromptTemplate.from_messages(MessageAddition)
parser = StrOutputParser()


individual_response=[]
# Session-safe tap that captures output
def tap(tag):
    def store_and_print(x):
        print(f"\n--- {tag} ---\n{x}\n")
        individual_response.append((tag, str(x)))  # Append tuple (tag, content) to individual_response
        return x  # Return x to allow chaining
    return RunnableLambda(store_and_print)

# Define the chain with intermediate taps
parallel_chain = RunnableParallel({
    "content1": prompt_content | modelGemini | parser | tap("Content1 (Gemini)"),
    "content2": prompt_content | modelCohere_r_plus | parser | tap("Content2 (Cohere R+)"),
    "content3": prompt_content | modelCohere_r | parser | tap("Content3 (Cohere R)"),
})

# Full chain with final aggregation tap
chain = (
    parallel_chain
    | prompt_addition
    | modelGemini
    | parser
    | tap("Final Aggregated Content")
)

if st.button("Generate"):
    # Clear previous responses to avoid duplicates
    individual_response.clear()
    
    # Run the chain
    response = chain.invoke({"topic": input_topic})
    
    # Display each response from individual_response
    for tag, content in individual_response:
        st.write(f"**{tag}**")
        st.write(content)
        st.write("---")  # Separator for readability