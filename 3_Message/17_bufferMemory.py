from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv

load_dotenv()

# Initialize memory with a window size of 5
memory = ConversationBufferWindowMemory(k=5, return_messages=True)

model = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

# Start with system message
messages = [SystemMessage(content="You are a helpful assistant.")]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break

    # Store user message in memory
    memory.chat_memory.add_message(HumanMessage(content=user_input))

    # Get last 5 messages from memory + system message
    messages = [SystemMessage(content="You are a helpful assistant.")] + memory.load_memory_variables({})["history"]

    # Invoke model
    response = model.invoke(messages)

    # Store AI response in memory
    memory.chat_memory.add_message(AIMessage(content=response))

    print(f"AI: {response}")

# Print final chat history
print("Chat History:", memory.load_memory_variables({})["history"])
