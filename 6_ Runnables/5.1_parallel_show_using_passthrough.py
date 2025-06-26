from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import traceback

load_dotenv()

# ========== MODELS ==========
modelGemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9, timeout=60, max_retries=3)
modelCohere_r_plus = ChatCohere(model="command-r-plus", temperature=0.9, timeout=60, max_retries=3)
modelCohere_r = ChatCohere(model="command-r", temperature=0.9, timeout=60, max_retries=3)

# ========== PROMPTS ==========
Message_Content = [
    ("system", "You are an AI Assistant for Content Generation. You will generate detailed content on the given topic. The content must be unique, easy to understand, and engaging. Use native-level English."),
    ("human", "Generate content for the topic {topic} in English Native Language")
]

Message_Addition = [
    ("system", "You are an advanced AI Assistant for Content Aggregation. Please aggregate all the contents in a sequenced, coherent, and on-topic manner. Respond in Native English."),
    ("human", "Aggregate the content as follows:\nContent1:\n{content1}\n\nContent2:\n{content2}\n\nContent3:\n{content3}")
]

prompt_content = ChatPromptTemplate.from_messages(Message_Content)
prompt_addition = ChatPromptTemplate.from_messages(Message_Addition)
parser = StrOutputParser()
# Define individual chains
chain1 = prompt_content | modelGemini | parser
chain2 = prompt_content | modelCohere_r_plus | parser
chain3 = prompt_content | modelCohere_r | parser


# Define content generation chain
content_chain = RunnableParallel({
    "content1": prompt_content | modelGemini | parser,
    "content2": prompt_content | modelCohere_r_plus | parser,
    "content3": prompt_content | modelCohere_r | parser
})

# Define aggregation chain
# RunnablePassthrough passes the entire input dictionary to prompt_addition
aggregation_chain = prompt_addition | modelGemini | parser

# Combine chains
parallel_chain = RunnableParallel({
    "contents": content_chain,  # Outputs {"content1": ..., "content2": ..., "content3": ...}
    "aggregate": content_chain | aggregation_chain  # Pass content_chain output to aggregation
})


# Invoke and get result
try:
    response = parallel_chain.invoke({"topic": "AI"})
    # print(response["content_gemini"]["content2"])  # Access content2 from content_gemini
    # print(response)
    print(response['contents'])
except Exception as e:
    print(f"Error: {e}")