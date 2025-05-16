from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage, HumanMessage, AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI


from dotenv import load_dotenv
load_dotenv()
# 1. Define your prompt template

message=[
    ("system", "You are a helpful {domain} assistant."),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human", "{input}"),
]

prompt_template = ChatPromptTemplate.from_messages(message)

# 2. Get user input for the domain

# 3. Initialize chat history
chat_history = []
with open('/home/shahanahmed/Zero_Shot_GenAI/Message/chat_history.txt') as f:
    history_str = f.read()

# Step 2: Safely evaluate with limited global namespace
chat_history = eval(history_str, {
    'SystemMessage': SystemMessage,
    'HumanMessage': HumanMessage,
    'AIMessage': AIMessage
})

# Now you have a list of Message objects
# print(chat_history)

domain = "general"
model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
file = open("/home/shahanahmed/Zero_Shot_GenAI/Message/chat_history.txt", "a")
# # 4. Start the chatbot loop
while True:
    input_query = input("Enter your query (or type 'exit' to quit): ")
    if input_query.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    elif input_query.lower() in ['domain','change']:
        domain=input("Enter Your Domain: ")
        input_query = input("Enter your query (or type 'exit' to quit): ")
    # 5. Format messages using the prompt template
    formatted_messages = prompt_template.format_messages(domain=domain, input=input_query)

    # 6. Extract system and human messages
    system_message = formatted_messages[0]
    human_message = formatted_messages[1]

    # 7. Append to chat history in correct order
    chat_history.append(system_message)
    chat_history.append(human_message)

    # 8. Invoke the model with full chat history
    response = model.invoke(chat_history)

    # 9. Add AI response to chat history
    ai_message = AIMessage(content=response.content)
    chat_history.append(ai_message)

    # 10. Print AI response
    print(f"Assistant: {ai_message.content}")
print(chat_history)
file.write(str(chat_history))
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import ast
from dotenv import load_dotenv

load_dotenv()

# 1. Define your prompt template
message = [
    ("system", "You are a helpful {domain} assistant."),
    ("human", "{input}")
]

prompt_template = ChatPromptTemplate.from_messages(message)

# Function to load chat history from file
def load_chat_history(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                # Check if file has content
                if content.strip():
                    # Create the chat history manually by parsing the content
                    chat_history = []
                    
                    # Parse each message type using regex pattern matching
                    import re
                    
                    # Pattern for SystemMessage
                    system_pattern = r"SystemMessage\(content='([^']*)'[^)]*\)"
                    system_messages = re.findall(system_pattern, content)
                    
                    # Pattern for HumanMessage
                    human_pattern = r"HumanMessage\(content='([^']*)'[^)]*\)"
                    human_messages = re.findall(human_pattern, content)
                    
                    # Pattern for AIMessage (this handles both single and double quotes)
                    ai_pattern = r"AIMessage\(content=['\"]([^'\"]*)['\"][^)]*\)"
                    ai_messages = re.findall(ai_pattern, content)
                    
                    # Reconstruct the conversation in order
                    # This assumes messages are in the order they appear in the file
                    message_indices = []
                    
                    for match in re.finditer(r"(SystemMessage|HumanMessage|AIMessage)\(", content):
                        message_type = match.group(1)
                        pos = match.start()
                        message_indices.append((pos, message_type))
                    
                    # Sort by position in file
                    message_indices.sort()
                    
                    # Use counters to track which message we're at in each list
                    sys_count = hum_count = ai_count = 0
                    
                    for _, msg_type in message_indices:
                        if msg_type == "SystemMessage" and sys_count < len(system_messages):
                            chat_history.append(SystemMessage(content=system_messages[sys_count]))
                            sys_count += 1
                        elif msg_type == "HumanMessage" and hum_count < len(human_messages):
                            chat_history.append(HumanMessage(content=human_messages[hum_count]))
                            hum_count += 1
                        elif msg_type == "AIMessage" and ai_count < len(ai_messages):
                            chat_history.append(AIMessage(content=ai_messages[ai_count]))
                            ai_count += 1
                    
                    print(f"Chat history loaded with {len(chat_history)} messages.")
                    return chat_history
                else:
                    print("Chat history file is empty. Starting with a new chat.")
                    return []
        else:
            print("Chat history file does not exist. Starting with a new chat.")
            return []
    except Exception as e:
        print(f"Error loading chat history: {e}")
        print("Starting with a new chat.")
        return []

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

# File path for chat history
history_file_path = "/home/shahanahmed/Zero_Shot_GenAI/Message/chat_history.txt"

# Load existing chat history if available
chat_history = load_chat_history(history_file_path)

# Extract the domain from the last system message if available
domain = "general"
for msg in reversed(chat_history):
    if isinstance(msg, SystemMessage):
        # Extract domain from the system message content
        content = msg.content
        if "You are a helpful" in content and "assistant" in content:
            try:
                domain = content.split("You are a helpful ")[1].split(" assistant")[0]
                print(f"Resumed with domain: {domain}")
                break
            except:
                pass

print(f"Current domain: {domain}")
print("Chat history loaded. You can continue your conversation.")
if chat_history:
    print("\nLast few messages:")
    # Display the last few messages for context
    max_display = min(6, len(chat_history))
    for i in range(len(chat_history) - max_display, len(chat_history)):
        msg = chat_history[i]
        if isinstance(msg, SystemMessage):
            print(f"System: {msg.content}")
        elif isinstance(msg, HumanMessage):
            print(f"You: {msg.content}")
        elif isinstance(msg, AIMessage):
            print(f"Assistant: {msg.content}")
    print("\n")

# Start the chatbot loop
while True:
    input_query = input("Enter your query (or type 'exit' to quit, 'domain' to change domain): ")
    
    if input_query.lower() in ["exit", "quit"]:
        print("Saving chat history and exiting. Goodbye!")
        with open(history_file_path, "w") as file:
            file.write(str(chat_history))
        break
    
    elif input_query.lower() in ['domain', 'change']:
        domain = input("Enter your domain: ")
        input_query = input("Enter your query (or type 'exit' to quit): ")
        if input_query.lower() in ["exit", "quit"]:
            print("Saving chat history and exiting. Goodbye!")
            with open(history_file_path, "w") as file:
                file.write(str(chat_history))
            break
    
    # Format messages using the prompt template
    formatted_messages = prompt_template.format_messages(domain=domain, input=input_query)
    
    # Extract system and human messages
    system_message = formatted_messages[0]
    human_message = formatted_messages[1]
    
    # Append to chat history
    chat_history.append(system_message)
    chat_history.append(human_message)
    
    # Invoke the model with full chat history
    try:
        response = model.invoke(chat_history)
        
        # Add AI response to chat history
        ai_message = AIMessage(content=response.content)
        chat_history.append(ai_message)
        
        # Print AI response
        print(f"Assistant: {ai_message.content}")
        
        # Save chat history after each interaction
        with open(history_file_path, "w") as file:
            file.write(str(chat_history))
            
    except Exception as e:
        print(f"Error occurred: {e}")
        # If error occurs, save the chat history up to this point
        with open(history_file_path, "w") as file:
            file.write(str(chat_history))