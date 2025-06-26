'''
pip install -U langchain langchain-experimental
'''

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os # os মডিউল ইম্পোর্ট করুন .env ফাইল থেকে ভেরিয়েবল লোড করার জন্য

load_dotenv() # .env ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করুন

# HuggingFaceEmbeddings মডেলটি লোড করা হচ্ছে।
# এই মডেলটি প্রশিক্ষণের সময় গ্রেডিয়েন্ট ডিসেন্ট ব্যবহার করেছে।
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

# অথবা আপনি OpenAIEmbeddings ব্যবহার করতে পারেন, যা OpenAI এর মডেল ব্যবহার করে।
# এই মডেলগুলিও প্রশিক্ষণের সময় গ্রেডিয়েন্ট ডিসেন্ট ব্যবহার করেছে।
# embedding = OpenAIEmbeddings() 

# SemanticChunker তৈরি করা হচ্ছে। এটি উপরে সংজ্ঞায়িত 'embedding' মডেলটি ব্যবহার করবে।
# breakpoint_threshold_type "standard_deviation" ব্যবহার করে, যা সিমিলারিটি স্কোরের পরিসংখ্যানগত বিশ্লেষণ।
# এটি সরাসরি গ্রেডিয়েন্ট ব্যবহার করে না, বরং গ্রেডিয়েন্ট-প্রশিক্ষিত এমবেডিং ব্যবহার করে।
text_splitter = SemanticChunker(
    embedding, # এখানে আপনার নির্বাচিত এমবেডিং মডেল পাস করা হচ্ছে
    breakpoint_threshold_type="gradient",
    breakpoint_threshold_amount=1
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])
print(f"Number of chunks: {len(docs)}")

for i in docs:
    print(i.page_content)

