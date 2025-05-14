from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate


chatTemplet=ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    ('human', "What is the {level} level of {input}?"),
])

prompt=chatTemplet.invoke({"domain":"AI", "input":"Python", "level":"easy"})

print(prompt)



