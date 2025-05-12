from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the greater of 5 and 3?"),
]

model= GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
response= model.invoke(messages)
messages.append(AIMessage(content=response))

print(messages)