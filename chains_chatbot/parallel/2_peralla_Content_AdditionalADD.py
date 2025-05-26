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


modelGemini= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9,
)
modelCohere= ChatCohere(
    model="command-r-plus",
    temperature=1.5,
)
modelGemma2= ChatOllama(
    model="gemma3:latest",
    temperature=1.5,
)

modellqwen= ChatOllama(
    model="qwen2.5-coder:latest",
    temperature=1.5,
)

modelDeepseek=ChatOllama(
    model="deepseek-r1:latest",
    temperature=1.5,
)


Message_Content=[
    ('system',"You are an AI Assistente for Content Generation. You will generate a Detailed content on the given topic. You will generate content in a way that it is unique and not copied from any source. You will generate content in a way that it is easy to understand and engaging for the user.Please Generate Content In Bangla Native Lanuage. You will generate content in a way that it is unique and not copied from any source. You will generate content in a way that it is easy to understand and engaging for the user. You will generate content in a way that it is unique and not copied from any source. You will generate content in a way that it is easy to understand and engaging for the user"),
    ('human', "Generate content for the topic {topic} in Bangla Native Language")
]

MessageAddition=[
    ('system',"You are an Advance AI Assisten for Content Aggrigation. Please Aggtigate all the contents in sequencial Manner. Please Make sure that All the contents are perfectly on topic and sequencial. Response your answer in Bangla Native Language"),
    ('human', "Aggtigate the content as follows {content1}, {content2}, {content3}, {content4}, {content5}")
]

prompt_content= ChatPromptTemplate.from_messages(Message_Content)
prompt_addition= ChatPromptTemplate.from_messages(MessageAddition)

parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        "content1": prompt_content | modelGemini | parser,
        "content2": prompt_content | modelCohere | parser,
        "content3": prompt_content | modelGemma2 | parser,
        "content4": prompt_content | modellqwen | parser,
        "content5": prompt_content | modelDeepseek | parser
    }
)
chain=parallel_chain | prompt_addition | modelGemini | parser


chain.get_graph().print_ascii()





