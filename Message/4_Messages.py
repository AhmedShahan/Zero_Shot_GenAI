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


## Printing Messages
print("System Message:", messages[0].content)
print("Human Message:", messages[1].content)
print("AI Message:", messages[2].content)


for message in messages:
    print(f"{message.__class__.__name__}: {message.content}")

# print(messages)
# Print each message type separately
# for message in messages:
#     if isinstance(message, SystemMessage):
#         print("System Message:", message.content)
#     elif isinstance(message, HumanMessage):
#         print("Human Message:", message.content)
#     elif isinstance(message, AIMessage):
#         print("AI Message:", message.content)
