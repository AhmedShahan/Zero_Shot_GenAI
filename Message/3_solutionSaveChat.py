from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model= GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
chat_history= []
while True:
    user_input= input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response= model.invoke(chat_history)
    chat_history.append(response)
    print(f"AI: {response}")

print("Chat History:", chat_history)

'''
Solution
সরাসরি ইউজার ইনপুট এবং AI রেসপন্স দুইটাই সেইভ না করে আমরা একটা ডিকশনারি সেইভ করে রাখতে পারি। 
এই কাজটা ম্যানুয়ালি না করে langchain এর মাধ্যমে সহজেই করা যায়।

This is Called "Message" in Langchain.
There are Three types of Messages in Langachain
1. Human Message
2. AI Message
3. System Message
'''