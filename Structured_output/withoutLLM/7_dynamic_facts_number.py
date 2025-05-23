from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)


message_template = [
    ('system', "You are a helpful AI Fact Generator. You must respond with valid JSON only."),
    ('human', f"""Generate a list of {{num_facts}} interesting facts about {{topic}}.

{{format_instructions}}

Important: Respond ONLY with valid JSON. Do not include any other text or explanation."""),
]

def create_dynamic_schema(num_facts):
    schema = [
        ResponseSchema(name="facts", description="List of facts about the topic"),
        ResponseSchema(name="summary", description="Summary of the facts"),
        ResponseSchema(name="conclusion", description="Conclusion based on the facts"), 
        ResponseSchema(name="keywords", description="Keywords related to the topic"),
    ]
    for i in range(1, num_facts + 1):
        schema.append(ResponseSchema(name=f"Fact_{i}", description=f"Fact {i} about the topic"))
    return schema

topic="Artificial Intelligence"
totalFacts=10
schema = create_dynamic_schema(totalFacts)
parser = StructuredOutputParser.from_response_schemas(schema)
format_instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_messages(message_template)

chain = prompt | model | parser

response = chain.invoke({
    "topic": topic,
    "num_facts": totalFacts,
    "format_instructions": format_instructions
})


# 🔄 Example usage
# print(response)
print("Facts:", response["facts"])
print("*"*100)
print("Summary:", response["summary"])
print("*"*100)
print("Conclusion:", response["conclusion"])
print("*"*100)
print("Keywords:", response["keywords"])
print("*"*100)

print("Facts:")
# Extract individual facts
for i in range(1, totalFacts+1):
    print(f"Fact {i}:", response[f"Fact_{i}"])
