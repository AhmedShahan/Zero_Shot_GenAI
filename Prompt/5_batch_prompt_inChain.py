from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

query="What is AI"

response=model.invoke(query)

print(response.content)