'''
Generate a report using the Gemini-1.5-flash model with chat-based prompts.
Generate 5/6/10 User input summary using Cohera AI model.
'''


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence



load_dotenv()
model1 = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

model2 = ChatCohere(
    model="command-r-plus",
    temperature=0.7
)

message1=[
    ('system',"You are a helpful AI Report Generator. Please Provide a Detailed recent Content of the following topic"),
    ('human',"Generate a detailed report on {topic}")
]

message2=[
    ('system', "You are an Helpful AI Summary Generator. Please Provide a Detailed, accurate and brief summary of the following report"),
    ('human', "Generate a summary of {report} in {lines} lines")
]


prompt1=ChatPromptTemplate.from_messages(message1)
prompt2=ChatPromptTemplate.from_messages(message2)

parser=StrOutputParser()


# Chain
def build_summary_inputs(report: str, lines: int = 5):
    return {"report": report, "lines": str(lines)}

# Final sequential chain
chain: RunnableSequence = (
    prompt1 
    | model1 
    | parser 
    | (lambda report_output: prompt2.format(**build_summary_inputs(report=report_output, lines=5)))
    | model2 
    | parser
)

chain.get_graph().print_ascii()

result = chain.invoke({"topic": "Recent advancements in Quantum Computing","lines":20})
print(result)