from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, create_model
from typing import List
import os

load_dotenv()

# 1. Dynamic model generator
def generate_facts_model(num_facts: int):
    fields = {
        'summary': (str, Field(..., description="The summary of the facts")),
        'keywords': (List[str], Field(..., description="Keywords related to the topic"))
    }
    for i in range(1, num_facts + 1):
        fields[f'facts{i}'] = (str, Field(..., description=f"Fact {i} about the topic"))

    return create_model(f'FactsFinder_{num_facts}', **fields)

# 2. Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

# 3. Prompt
message_template = [
    ('system', "You are a helpful AI Fact Generator. You must respond with valid JSON only."),
    ('human', """Generate a list of {num_facts} interesting facts about {topic}.

{format_instructions}

Important: Respond ONLY with valid JSON. Do not include any other text or explanation."""),
]

# 4. Parameters
topic = "Artificial Intelligence"
num_facts = 10

# 5. Generate dynamic model & parser
DynamicFactsModel = generate_facts_model(num_facts)
parser = PydanticOutputParser(pydantic_object=DynamicFactsModel)
format_instructions = parser.get_format_instructions()

# 6. Prompt + model + parser chain
prompt = ChatPromptTemplate.from_messages(message_template)
chain = prompt | model | parser

# 7. Invoke
response = chain.invoke({
    "topic": topic,
    "num_facts": num_facts,
    "format_instructions": format_instructions
})

# 8. Output
print(response)
