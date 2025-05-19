### Some Phone information
from typing import TypedDict, Annotated, Optional


## Basic Workflow
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()



model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)


phone_review="""
I recently switched to the Samsung Galaxy A55, and using it for a few weeks has given me a fairly complete impression. The design is modern with a smooth matte finish that doesn't attract fingerprints easily. The 6.6-inch Super AMOLED display delivers punchy colors and deep contrast, making video content enjoyable even in bright daylight. Scrolling through apps feels fluid thanks to the 120Hz refresh rate, which is especially nice when browsing or gaming.

One aspect that stood out to me is the battery. With moderate use, the phone comfortably lasts more than a day on a single charge. I appreciated the inclusion of stereo speakers as well; they offer decent clarity when watching YouTube or playing music. The UI feels clean, and One UI 6.1 brings small enhancements that make navigation smooth without feeling bloated. There's also an in-display fingerprint scanner that works reliably and quickly.

On the flip side, performance occasionally shows its limits. The Exynos 1480 chip handles day-to-day tasks well, but there are occasional hiccups when running more demanding apps or switching between multiple games. The camera does well in daylight, but low-light results tend to be soft and lack consistency. Moreover, the absence of wireless charging and a charger in the box made setup a bit inconvenient. For a mid-range phone, I had hoped for more flexibility in this regard.

In terms of overall experience, it strikes a balance between style, screen quality, and practicality. It’s clear the phone is aimed at users who prioritize display and battery, while those expecting flagship-level photography or raw power might need to look elsewhere.
Experience Impression: Balanced, leaning toward appreciation with reservations

"""


television_review="""
After spending a few weeks with the LG C3 OLED TV, I’ve had the chance to explore both its strengths and the areas where it could improve. The first thing that grabs attention is the ultra-thin profile—it almost disappears when wall-mounted, giving the room a sleek and modern look. The 4K OLED panel delivers remarkable picture quality. Dark scenes in movies have a cinematic depth, with inky blacks and rich contrast that add realism to every frame. Watching nature documentaries or high-definition sports broadcasts is equally stunning, with colors appearing vibrant but not oversaturated.

The webOS interface feels intuitive, and switching between apps like Netflix, YouTube, and Prime Video happens quickly without noticeable lag. The Magic Remote takes some getting used to but becomes natural after a day or two. Another noticeable point is the sound. While it doesn’t replace a dedicated sound system, the built-in speakers are surprisingly clear, especially for dialogue-heavy content. The AI Sound Pro feature adjusts levels based on content type, which proves helpful during quiet conversations and action scenes alike.

However, brightness during the day could be better. In rooms with a lot of sunlight, reflections sometimes interfere with visibility, especially on lighter scenes. For gaming, while the 120Hz refresh rate and HDMI 2.1 support are great additions, there have been occasional compatibility issues when connecting older consoles. Also, some users might find the setup process a bit lengthy, particularly if calibrating the picture manually.

Altogether, this TV seems designed for viewers who value visual precision and style, with a clear focus on cinematic quality and smart integration. It's built to impress in darkened environments and delivers a viewing experience that’s hard to forget.
Experience Impression: Strong visual appeal with minor usability trade-offs

"""

class Review(TypedDict):
    key_features:Annotated[list[str], "Write down all the key features discussed about the phone."]
    summary:Annotated[str, "A brief summary of teh product in easy way with in 100 Words"]
    sentiment:Annotated[str, "Return the sentiment of the reviewer either positive or negative"]
    pros: Annotated[Optional[list[str]], "Write Down all the Pros from the review in a List"]
    cons: Annotated[Optional[list[str]], "Write Down all the Cons from the review in a List"]

structured_model=model.with_structured_output(Review)

response=structured_model.invoke(television_review)
print("Key Features: ", response["key_features"])
print("Summary: ", response["summary"])
print("Sentiment: ", response["sentiment"])
print("Pros: ", response["pros"])
print("Cons: ", response["cons"])










####### Response Analysis
'''
Original
Key Features:
4K OLED display with perfect blacks and vibrant colors

Ultra-slim design, ideal for wall mounting

webOS smart platform with smooth app switching

Magic Remote with motion control support

AI Sound Pro technology for adaptive audio enhancement

120Hz refresh rate + HDMI 2.1 (supports next-gen gaming)

Dolby Vision and Dolby Atmos support for cinematic experience

📝 Summary:
A premium OLED TV designed for those who value high-end visuals, smart features, and elegant aesthetics. It excels in dark room performance, offers smooth navigation, and is well-suited for streaming and gaming. A few usability issues are present, but they don’t significantly affect the overall quality.

✅ Pros:
Stunning picture quality with deep contrast

Clean, modern look with ultra-thin build

Intuitive and fast user interface

Good sound without external speakers

Strong support for gamers (high refresh rate, HDMI 2.1)

❌ Cons:
Reflective screen in bright environments

Slight learning curve with Magic Remote

Manual picture calibration can be time-consuming

No bundled soundbar or high-end speaker system

🎯 Sentiment:
Positive


-------------------------------------------------

This code response
Key Features:  ['"4K OLED panel"', '"webOS interface"', '"AI Sound Pro"', '"120Hz refresh rate"', '"HDMI 2.1 support"', '"Magic Remote"']
Summary:  "Strong visual appeal with minor usability trade-offs"
Sentiment:  "Positive"
Pros:  ['"Ultra-thin profile"', '"Remarkable picture quality with inky blacks and rich contrast"', '"Vibrant colors in nature documentaries and sports broadcasts"', '"Intuitive webOS interface with quick app switching"', '"Surprisingly clear built-in speakers"', '"AI Sound Pro feature adjusts levels based on content type"', '"120Hz refresh rate and HDMI 2.1 support for gaming"']
Cons:  ['"Brightness could be better in sunlight"', '"Reflections interfere with visibility in bright rooms"', '"Occasional compatibility issues with older gaming consoles"', '"Lengthy setup process, especially with manual picture calibration"']





'''