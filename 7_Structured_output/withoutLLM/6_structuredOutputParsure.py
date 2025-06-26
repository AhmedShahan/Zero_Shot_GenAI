from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


message_template = [
    ('system', "You are a helpful AI Fact Generator. You must respond with valid JSON only."),
    ('human', """Generate a list of 3 interesting facts about {topic}.

{format_instructions}

Important: Respond ONLY with valid JSON. Do not include any other text or explanation."""),
]
prompt = ChatPromptTemplate.from_messages(message_template)


model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7  # Reduced temperature for more consistent formatting
)


# Define the response schema
schema = [
    ResponseSchema(name="facts", description="List of facts about the topic"),
    ResponseSchema(name="summary", description="Summary of the facts"),
    ResponseSchema(name="conclusion", description="Conclusion based on the facts"), 
    ResponseSchema(name="keywords", description="Keywords related to the topic"),
    ResponseSchema(name="Fact_1", description="Fact 1 About the Topic"),
    ResponseSchema(name="Fact_2", description="Fact 2 About the Topic"),
    ResponseSchema(name="Fact_3", description="Fact 3 About the Topic"),
]

# Create the parser and get format instructions
parser = StructuredOutputParser.from_response_schemas(schema)
format_instructions = parser.get_format_instructions()


chain = prompt | model | parser

# Invoke the chain
response = chain.invoke({
    "topic": "Artificial Intelligence",
    "format_instructions": format_instructions
})

# print("Facts:", response["facts"])
# print("Summary:", response["summary"])
# print("Conclusion:", response["conclusion"])
# print("Keywords:", response["keywords"])

print(response)