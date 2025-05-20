from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()


model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)

prompt="write down the summary of Attendtion All you Need Paper"

summary = model.invoke(prompt)

print(summary.content)