from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

messages=[
    SystemMessage(content="You are a helpful assistant."),
]

promprt="What is The Greater of 5 and 3?"
messages.append(HumanMessage(content=promprt))
model= GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
response= model.invoke(messages)
messages.append(AIMessage(content=response))

print("Chat History:", messages)
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
