'''
Main Target is : 
Generate a Report using LLM model with chat prompt template.
The Report will be summarized in 10/ 20 User defined Lines Lines
Structured the Summary with: 
                    1. Keywords
                    2. Summary
                    3. Conclusion
'''


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Define the message template
Message1 = [
    ('system', "You are a helpful AI Report Generating assistant."),
    ('human', "Generate a detailed report on {topic} including its history, current trends, and future prospects."),
]
Message2 = [
    ('system', "You are a helpful AI Report Summarizer."),
    ('human', "Summarize the following report: {report} within {lines} lines"),
]

Message3 = [
    ('system', "You are a helpful AI Report Structurer."),
    ('human', "Structure the following report summary into keywords, summary ({final_lines} lines), and conclusion ({conc_lines} lines): {report_summary}"),
]

# Create a ChatPromptTemplate
prompt1 = ChatPromptTemplate.from_messages(Message1)
prompt2 = ChatPromptTemplate.from_messages(Message2)
prompt3 = ChatPromptTemplate.from_messages(Message3)

# Instantiate Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)
parser = StrOutputParser()

# Define the chain - FIXED VERSION
chain = (
    RunnablePassthrough.assign(
        report=(prompt1 | model | parser)
    ) |
    RunnablePassthrough.assign(
        report_summary=(prompt2 | model | parser)
    ) |
    (prompt3 | model | parser)
)

# Invoke the chain with the topic and lines
response = chain.invoke({
    "topic": "Artificial Intelligence",
    "lines": 20,
    "final_lines": 10,
    "conc_lines": 5
})

print("Report:", response)