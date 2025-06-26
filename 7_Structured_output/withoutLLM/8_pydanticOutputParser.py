from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)


message_template = [
    ('system', "You are a helpful AI Fact Generator. You must respond with valid JSON only."),
    ('human', f"""Generate a list of 3 interesting facts about {{topic}}.

{{format_instructions}}

Important: Respond ONLY with valid JSON. Do not include any other text or explanation."""),
]

class FactsFinder(BaseModel):
    summary: str = Field(description="The summary of The facts")
    keywords: list[str] = Field(description="Keywords related to the topic")
    facts1: str = Field(description="Fact 1 about the topic")
    facts2: str = Field(description="Fact 2 about the topic")
    facts3: str = Field(description="Fact 3 about the topic")


parser=PydanticOutputParser(pydantic_object=FactsFinder)
topic="Artificial Intelligence"
format_instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_messages(message_template)

chain = prompt | model | parser

response = chain.invoke({
    "topic": topic,
    "format_instructions": format_instructions
})


# 🔄 Example usage
# print(response)
print(response)



