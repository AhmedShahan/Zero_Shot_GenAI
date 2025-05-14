from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate


chatTemplet=ChatPromptTemplate([
    SystemMessage(content="You are a {domain} assistant."),
    HumanMessage(content="Explain {input} in detail in {level}"),
])

prompt=chatTemplet.invoke({"domain":"AI", input:"Python", "level":"easy"})

print(prompt)



