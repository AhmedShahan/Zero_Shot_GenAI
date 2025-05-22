### Some Phone information
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Literal

## Basic Workflow
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()



model = ChatOllama(model="deepseek-r1:1.5b")

# model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.5
# )
# ### 

### Cemini is not working


phone_review="""
I recently switched to the Samsung Galaxy A55, and using it for a few weeks has given me a fairly complete impression. The design is modern with a smooth matte finish that doesn't attract fingerprints easily. The 6.6-inch Super AMOLED display delivers punchy colors and deep contrast, making video content enjoyable even in bright daylight. Scrolling through apps feels fluid thanks to the 120Hz refresh rate, which is especially nice when browsing or gaming.

One aspect that stood out to me is the battery. With moderate use, the phone comfortably lasts more than a day on a single charge. I appreciated the inclusion of stereo speakers as well; they offer decent clarity when watching YouTube or playing music. The UI feels clean, and One UI 6.1 brings small enhancements that make navigation smooth without feeling bloated. There's also an in-display fingerprint scanner that works reliably and quickly.

On the flip side, performance occasionally shows its limits. The Exynos 1480 chip handles day-to-day tasks well, but there are occasional hiccups when running more demanding apps or switching between multiple games. The camera does well in daylight, but low-light results tend to be soft and lack consistency. Moreover, the absence of wireless charging and a charger in the box made setup a bit inconvenient. For a mid-range phone, I had hoped for more flexibility in this regard.

In terms of overall experience, it strikes a balance between style, screen quality, and practicality. It’s clear the phone is aimed at users who prioritize display and battery, while those expecting flagship-level photography or raw power might need to look elsewhere.
Experience Impression: Balanced, leaning toward appreciation with reservations

"""


json_schema={
    "title": "Phone Review",
    "description": "A review of a phone with its features and performance",
    "type": "object",
    "properties": {
        "key_terms": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Key terms discussed in the review"
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the product in an easy way within 100 words"
        },
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "The sentiment of the reviewer, either positive or negative"
        },
        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Pros from the review"
        },
        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Cons from the review"
        },
        "reviewer_name": {
            "type": ["string"],
            "description": "Name of the reviewer"
        }
    },
    "required": ["key_terms", "summary", "sentiment", "pros", "cons", "reviewer_name"]

}


structured_output_model=model.with_structured_output(json_schema)
response=structured_output_model.invoke(phone_review)
print(response)