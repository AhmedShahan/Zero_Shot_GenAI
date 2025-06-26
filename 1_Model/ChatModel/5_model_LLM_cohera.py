'''
pip install langchain-cohere cohere
'''

from dotenv import load_dotenv
import os

load_dotenv()
from langchain_cohere import ChatCohere

llm = ChatCohere(model="command-r-plus")
response = llm.invoke("Tell me a joke about a cat.")

print(response.content)

'''
১. পুরনো ধরনের LLM (যেটা এখন কাজ করে না):
python
Copy
Edit
# এটা এখন আর কাজ করে না
from langchain_cohere import Cohere

llm = Cohere(model="command-r")
response = llm.invoke("একটা গল্প বলো।")
❌ এটা Error দিবে, কারণ Cohere এখন চ্যাট ফরম্যাটে কাজ করে।

২. নতুন সিস্টেম (ChatCohere):
python
Copy
Edit
from langchain_cohere import ChatCohere

llm = ChatCohere(model="command-r-plus")
response = llm.invoke("একটা গল্প বলো।")

print(response.content)
✅ এটা কাজ করবে, কারণ Cohere এখন শুধু Chat ফরম্যাটে কাজ করে।

🔁 তাহলে পার্থক্য কী?
বিষয়	পুরনো Cohere()	নতুন ChatCohere()
ইনপুট টাইপ	সাধারণ string	chat-style message
এখন কাজ করে কি?	❌ না	✅ হ্যাঁ
মডেল আলাদা?	❌ না (একই মডেল)	❌ না (একই মডেল)

🔥 সবচেয়ে গুরুত্বপূর্ণ কথা:
এখন command-r আর command-r-plus – এই মডেলগুলা শুধু Chat ফরম্যাটে কাজ করে। তাই ChatCohere ব্যবহার করতে হবে।
'''