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

model= GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
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

'''
You: Hi
AI: Hi there! How can I help you today?
You: What is the largest of 20, 21, 40, 5, 65, 27, 8 
AI: The largest number in that list is 65.
You: multiply 5 with largest number
AI: AI: 5 multiplied by 65 is 325.
You: divide by 5
AI: AI: 325 divided by 5 is 65.
You: exit
Exiting the chatbot. Goodbye!
Chat History: [SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Hi', additional_kwargs={}, response_metadata={}), AIMessage(content='Hi there! How can I help you today?', additional_kwargs={}, response_metadata={}), HumanMessage(content='What is the largest of 20, 21, 40, 5, 65, 27, 8', additional_kwargs={}, response_metadata={}), AIMessage(content='The largest number in that list is 65.', additional_kwargs={}, response_metadata={}), HumanMessage(content='multiply 5 with largest number', additional_kwargs={}, response_metadata={}), AIMessage(content='AI: 5 multiplied by 65 is 325.', additional_kwargs={}, response_metadata={}), HumanMessage(content='divide by 5', additional_kwargs={}, response_metadata={}), AIMessage(content='AI: 325 divided by 5 is 65.', additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]
'''