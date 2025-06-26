'''
Exactly Parallel Chain

'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

modelGemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)
modelCohere_r_plus = ChatCohere(model="command-r-plus", temperature=0.9)
modelCohere_r = ChatCohere(model="command-r", temperature=0.9)

Message_Content = [
    ('system', "You are an AI Assistant for Content Generation. You will generate detailed content on the given topic. "
               "Generate content in English native language. Make sure the content is unique, easy to understand, and engaging."),
    ('human', "Generate content for the topic {topic} in Bangla native language.")
]

MessageAddition = [
    ('system', "You are an advanced AI Assistant for Content Aggregation. Please aggregate all the contents in sequential manner. "
               "Make sure that all the contents are perfectly on topic and sequential. Respond in Bangla native language."),
    ('human', "Aggregate the content as follows {content1}, {content2}, {content3}.")
]

prompt_content = ChatPromptTemplate.from_messages(Message_Content)
prompt_addition = ChatPromptTemplate.from_messages(MessageAddition)
parser = StrOutputParser()



# Parallel generation with taps
parallel_chain = RunnableParallel({
    "content1": prompt_content | modelGemini | parser,
    "content2": prompt_content | modelCohere_r_plus | parser,
    "content3": prompt_content | modelCohere_r | parser,
})

# Full chain with final tap
chain = parallel_chain | prompt_addition | modelGemini | parser

# Run it
result = chain.invoke({"topic": "What is AI"})

print(result)