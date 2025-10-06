### Create a Simple Terminal based chatbot using Gemini. 
'''
You: Hi
AI: Hello! How can I assist you today?
You: What is the capital of France?
AI: The capital of France is Paris.
'''


from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model= GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
while True:
    user_input= input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response= model.invoke(user_input)
    print(f"AI: {response}")

'''
Problem in thsi chatbot
You: What is teh greater of 5 and 3
AI: 5 is greater than 3.
You: Multiply 3 with largest number
AI: The largest number is undefined.  There is no largest number.  Therefore, it's impossible to multiply 3 by the largest number.

এখানে চ্যাট শেভ করে সেটা ব্যবহার করা হচ্ছে না। তাই আমাদের চ্যাট শেভ করে রাখতে হবে। 
'''