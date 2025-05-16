from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI


from dotenv import load_dotenv
load_dotenv()
# 1. Define your prompt template

message=[
    ("system", "You are a helpful {domain} assistant."),
    ("human", "{input}")
]

prompt_template = ChatPromptTemplate.from_messages(message)

# 2. Get user input for the domain
domain = "general"

# 3. Initialize chat history
chat_history = []


file = open("/home/shahanahmed/Zero_Shot_GenAI/Message/chat_history.txt", "w")

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
# 4. Start the chatbot loop
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
