'''
First we will Generate Content using a LLM model with chat prompt templet. 
Colelct the content
Generate teh summary of that content using same model with different prompt template



########### Using StrOutPutParser ##################
'''


from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
# Load environment variables (for Gemini API key)
load_dotenv()

# Define the message template
Message1 = [
    ('system', "You are a helpful AI Report Generating assistant."),
    ('human', "Generate a detailed report on {topic} including its history, current trends, and future prospects."),

]

Message2=[
    ('system', "You are a helpful AI Report Summarizer."),
    ('human', "Summarize the following report: {report} within {lines} lines"),
    ### যদি আমরা সেকেন্ড মেসেজ এ কোনও কিছু পাঠাতে চাই তাহলে সেটার জপনয় Ruuanble lambda লাগবে। সেটা পরে দেখবো 
]

# Create a ChatPromptTemplate
prompt1 = ChatPromptTemplate.from_messages(Message1)
prompt2 = ChatPromptTemplate.from_messages(Message2)
# Instantiate Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)
parser=StrOutputParser()

chain= (
    {
        "report": prompt1 | model | parser,
        "lines": lambda x: x["lines"]
    }
    | prompt2 | model | parser
)

response=chain.invoke({"topic": "Artificial Intelligence", "lines": 20})
print("Report:", response)
