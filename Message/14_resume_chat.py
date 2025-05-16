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
