### Some Phone information
from typing import TypedDict


## Basic Workflow
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()



model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)

prompt="""
The Galaxy S24 Ultra combines a titanium frame with a stunning QHD+ AMOLED display that makes visuals pop. 
The Snapdragon 8 Gen 3 chip ensures top-tier performance, and the 200MP camera offers unparalleled detail and zoom capabilities. 
Its S Pen integration is seamless for productivity, though the phone’s large size may not appeal to everyone, 
and its price remains high.
"""


class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review)
response=structured_model.invoke(prompt)
print(response['sentiment'])