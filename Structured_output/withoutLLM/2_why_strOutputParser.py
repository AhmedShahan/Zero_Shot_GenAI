from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables (for Gemini API key)
load_dotenv()

# Define the message template
Message1 = [
    ('system', "You are a helpful AI Report Generating assistant."),
    ('human', "Generate a detailed report on {topic} including its history, current trends, and future prospects."),

]

# Create a ChatPromptTemplate
prompt1 = ChatPromptTemplate.from_messages(Message1)

# Instantiate Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)

# Create the chain using LCEL
chain = prompt1 | model

# Invoke the chain with the topic variable
report = chain.invoke({"topic": "Artificial Intelligence"})

# Print the generated report
print("Report:", report.content)

### Ready to Generating The Report Summary
Message2=[
    ('system', "You are a helpful AI Report Summarizer."),
    ('human', "Summarize the following report: {report} within 5 line"),
]

prompt2 = ChatPromptTemplate.from_messages(Message2)
chain2=prompt2 | model
summary=chain2.invoke({"report": report.content})
print("\n\n")
print("*"*100)
print("Summary:", summary.content)

