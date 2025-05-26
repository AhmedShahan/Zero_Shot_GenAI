'''
Idea is all about.
User Will give an Topic
There parallally multiple (5 LLM) LLM will generate content on that topic
Thre an LLM will just Add new content if there available in the contens
'''


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
st.set_page_config(
    page_title="AI BlogCraft",
    layout="wide",
)

# st.set_page_config(page_title="Parallel Content Generation", page_icon=":robot_face:")
st.title("Parallel Content Generation with Multiple LLMs")

input_topic= st.text_input("Enter the topic for content generation:", "বাংলাদেশের ইতিহাস ও সংস্কৃতি")



modelGemini= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9,
)
modelCohere_r_plus= ChatCohere(
    model="command-r-plus",
    temperature=0.9,
)
modelCohere_r= ChatCohere(
    model="command-r",
    temperature=0.9,
)


Message_Content=[
    ('system',"You are an AI Assistente for Content Generation. You will generate a Detailed content on the given topic. You will generate content in a way that it is unique and not copied from any source. You will generate content in a way that it is easy to understand and engaging for the user.Please Generate Content In Bangla Native Lanuage. You will generate content in a way that it is unique and not copied from any source. You will generate content in a way that it is easy to understand and engaging for the user. You will generate content in a way that it is unique and not copied from any source. You will generate content in a way that it is easy to understand and engaging for the user"),
    ('human', "Generate content for the topic {topic} in Bangla Native Language")
]

MessageAddition=[
    ('system',"You are an Advance AI Assisten for Content Aggrigation. Please Aggtigate all the contents in sequencial Manner. Please Make sure that All the contents are perfectly on topic and sequencial. Response your answer in Bangla Native Language"),
    ('human', "Aggtigate the content as follows {content1}, {content2}, {content3}")
]

prompt_content= ChatPromptTemplate.from_messages(Message_Content)
prompt_addition= ChatPromptTemplate.from_messages(MessageAddition)

def Printing_c1():
    st.write("Content from Model Gemini")



parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        "content1": prompt_content | modelGemini | parser,
        "content2": prompt_content | modelCohere_r_plus | parser,
        "content3": prompt_content | modelCohere_r | parser,
    }
)
chain=parallel_chain | prompt_addition | modelGemini | parser


# chain.get_graph().print_ascii()
if st.button("Generate Content"):
    with st.spinner("Generating content..."):
        response = chain.invoke({
            "topic": input_topic
        })

