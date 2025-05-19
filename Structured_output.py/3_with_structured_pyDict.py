### Some Phone information
from typing import TypedDict


## Basic Workflow
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()



model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)


### Cohera
# model= ChatCohere(model="command-r-plus")
## Not work with with_structured. 

### 
# model=ChatOllama(model="deepseek-r1:1.5b")
# model=ChatOllama(model="phi4-mini")
model=ChatOllama(model="llama3.2:1b")





Samsung_Galaxy_S24_Ultra="""
The Galaxy S24 Ultra combines a titanium frame with a stunning QHD+ AMOLED display that makes visuals pop. 
The Snapdragon 8 Gen 3 chip ensures top-tier performance, and the 200MP camera offers unparalleled detail and zoom capabilities. 
Its S Pen integration is seamless for productivity, though the phone’s large size may not appeal to everyone, 
and its price remains high.
"""


iPhone_15="""
The iPhone 15 brings minor but welcome updates like a USB-C port and slightly better battery life. 
The Dynamic Island feature adds a playful touch, and iOS continues to offer a clean user experience. 
However, it feels too similar to the previous model, and the lack of a high-refresh-rate display might 
disappoint tech-savvy users expecting more innovation.

"""

OnePlus_Nord_CE_3_Lite="""
While the Nord CE 3 Lite offers a large 120Hz screen and decent battery life, 
it struggles to stand out in its price segment. The camera setup feels underwhelming with inconsistent results, 
and performance can lag under heavy multitasking. The build feels plasticky, and OxygenOS is starting to lose the 
simplicity that once defined it.
"""

class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review)

response_samsang=structured_model.invoke(Samsung_Galaxy_S24_Ultra)
response_iphone=structured_model.invoke(iPhone_15)
response_oneplus=structured_model.invoke(OnePlus_Nord_CE_3_Lite)


print("Review of Samsang")
print(response_samsang["summary"])
print(response_samsang["sentiment"])
print("*"*50)

print("Review of iphone")
print(response_iphone["summary"])
print(response_iphone["sentiment"])
print("*"*50)

print("Review of Onepus")
print(response_oneplus["summary"])
print(response_oneplus["sentiment"])
print("*"*50)


