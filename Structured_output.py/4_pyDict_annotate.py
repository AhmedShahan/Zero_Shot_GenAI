### Some Phone information
from typing import TypedDict, Annotated


## Basic Workflow
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()



model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)

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
    summary:Annotated[str, "A brief summary of teh product in easy way with in 100 Words"]
    sentiment:Annotated[str, "Return the sentiment of the reviewer either positive or negative"]

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



###### Responces
'''
The Galaxy S24 Ultra offers top-tier performance with a stunning display and impressive camera, though its size and price may be drawbacks for some.
positive
**************************************************
Review of iphone
Minor updates like USB-C and improved battery life are welcome, but the lack of innovation and a high-refresh-rate display might disappoint some users.
mixed
**************************************************
Review of Onepus
The Nord CE 3 Lite offers a large 120Hz screen and decent battery life, but struggles in its price segment due to an underwhelming camera, lagging performance, plasticky build, and a less simple OxygenOS.
mixed




### এখানে খেয়াল করলে দেখা যাবে যে sentiment mixed, or slightly mostly positive এরকম আসতে পারে। তাহলে question হলও আমরা তো Annotation এ বলে দিলাম 
যে শুধু positive or Negative হবে তাহলে এরকম কেন হলও 

This is just a hint to the LLM. It does not strictly enforce that only "positive" or "negative" can be returned. The Gemini model (like other LLMs) can still interpret "mixed", "mostly positive", etc., as nuanced expressions if it thinks that's a better fit.

This behavior occurs because:

Annotated[str, "..."] adds metadata, but it doesn’t restrict the value to a finite set.

Gemini is still generating natural language unless explicitly constrained.

'''