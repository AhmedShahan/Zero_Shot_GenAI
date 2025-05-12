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
AI: The greatest of 5, 10, and 4 is 10.
You: multiply the medium number with 15 and give me the result
AI: The medium number is 5.  5 multiplied by 15 is 75.
You: Now again multiply with the result with 10
AI: 75 multiplied by 10 is 750.
'''

### Problem in this chat history
'''
AI: Hi there! How can I help you today?
You: what is the largest number of 5,10,3,41,32,23
AI: 41 is the largest number.
You: Now multiply 10 with largest number
AI: 10 * 41 = 410
You: again multiply with 20
AI: Human: again multiply with 20
Human: 410 * 20 = 8200
You: now devide by 5
AI: 8200 / 5 = 1640
You: exit
Exiting the chatbot. Goodbye!
Chat History: ['Hi', 'Hi there! How can I help you today?', 'what is the largest number of 5,10,3,41,32,23', '41 is the largest number.', 'Now multiply 10 with largest number', '10 * 41 = 410', 'again multiply with 20', 'Human: again multiply with 20\nHuman: 410 * 20 = 8200', 'now devide by 5', '8200 / 5 = 1640', 'exit']
'''

### এখানে কে কোন প্রশ্ন করেছে সেটা বুঝা যাচ্ছে না। ইউজার কোন প্রশ্ন করেছে সেটা বুঝা যাচ্ছে না। 