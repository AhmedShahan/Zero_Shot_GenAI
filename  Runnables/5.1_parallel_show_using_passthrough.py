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

# Define aggregation chain to use outputs of other chains
def format_aggregation_inputs(inputs):
    try:
        return {
            "content1": inputs.get("content1", "Error: Content1 not generated"),
            "content2": inputs.get("content2", "Error: Content2 not generated"),
            "content3": inputs.get("content3", "Error: Content3 not generated")
        }
    except Exception as e:
        print(f"Error in format_aggregation_inputs: {str(e)}")
        raise

aggregation_chain = format_aggregation_inputs | prompt_addition | modelGemini | parser

# Combine chains in parallel
parallel_chain = RunnableParallel({
    "content1": chain1,
    "content2": chain2,
    "content3": chain3,
    "aggregate": aggregation_chain
})

# Invoke with error handling
try:
    response = parallel_chain.invoke({"topic": "AI"})
    # print(response)
except Exception as e:
    print(f"Error during invocation: {str(e)}")
    traceback.print_exc()

# Test chain1 independently
# print("\nTesting chain1 independently:")
# try:
#     result = chain1.invoke({"topic": "AI"})
#     print("Chain1 output:", result)
# except Exception as e:
#     print(f"Error in chain1: {str(e)}")
#     traceback.print_exc()

print(response["content2"])