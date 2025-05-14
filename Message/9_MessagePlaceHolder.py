from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessage(content="{user_input}"),
])

chat_history = [
    HumanMessage(content="What is AI?"),
    AIMessage(content="AI stands for Artificial Intelligence..."),
    HumanMessage(content="What are some applications of AI?"),
    AIMessage(content="Applications include self-driving cars, chatbots...")
]

latest_user_input = "Give a summary of the above conversation."

final_messages = prompt.format_messages(
    chat_history=chat_history,
    user_input=latest_user_input
)

# এখন দেখে নিই!
for msg in final_messages:
    print(f"{msg.__class__.__name__}: {msg.content}")
