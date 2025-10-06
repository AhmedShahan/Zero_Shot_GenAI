### Create a Simple Terminal based chatbot using Gemini. 
'''
You: Hi
AI: Hello! How can I assist you today?
You: What is the capital of France?
AI: The capital of France is Paris.
'''


from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

messages=[
    SystemMessage(content="You are a helpful assistant."),
]

model= GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
while True:
    user_input= input("You: ")
    messages.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response= model.invoke(messages)
    messages.append(AIMessage(content=response))
    print(f"AI: {response}")

print("Chat History:", messages)