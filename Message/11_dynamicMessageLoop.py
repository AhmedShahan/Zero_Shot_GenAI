from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Create a separate list to track chat history
chat_history = []

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=1.5)

# Define the message template
Message = [
    ('system', "You are a helpful {domain} assistant."),
    ('human', "{input}"),
]

domain = input("Enter the domain: ")

# Initialize the system message dynamically using the template
prompt_template = ChatPromptTemplate.from_messages(Message)

# Add the formatted system message to chat history

while True:
    input_query = input("Enter your query (or type 'exit' to quit): ")
    if input_query.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    formatted_messages = prompt_template.invoke({"domain": domain, "input":input_query}).messages

    systemMessage=SystemMessage(formatted_messages[0])
    human_message=HumanMessage(formatted_messages[1])
    chat_history.append(human_message)
    chat_history.append(systemMessage)
    # chat_history.append(formatted_messages[0])
    # Create a human message and add to history
    
    # Create a prompt from the current chat history
    current_messages = []
    for msg in chat_history:
        if isinstance(msg, SystemMessage):
            current_messages.append(("system", msg.content))
        elif isinstance(msg, HumanMessage):
            current_messages.append(("human", msg.content))
        elif isinstance(msg, AIMessage):
            current_messages.append(("ai", msg.content))
    
    # Create new prompt with the full history
    current_prompt = ChatPromptTemplate.from_messages(current_messages)
    
    # Invoke the chain and get the response
    chain = current_prompt | model
    response = chain.invoke({"domain": domain, "input":chat_history})
    
    # Add the AI response to chat history
    ai_message = AIMessage(content=response.content)
    chat_history.append(ai_message)
    
    # Print the response
    # print(response.content)

# Print the final chat history
# print("\nChat History:")
# for msg in chat_history:
#     print(f"{msg.type}: {msg.content}")

print("\nChat History:")
print(chat_history)