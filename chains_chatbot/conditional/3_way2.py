'''
Base Idea
From a Feedback
Analyze the feedback and return
    positive or Negative
'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

modelGemini=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)
modelCohere=ChatCohere(
    model="command-r-plus",
    temperature=0.9
)

Message_Content=[
    ('system', "You are AI Assitent which will Help to Analyze the Feedback and return the Positive or Negative Feedback."),
    ('human', "Analyze the feedback and return the Positive or Negative Feedback for the following content {content} and feedback.{format_instructions}"),
]


prompt=ChatPromptTemplate.from_messages(Message_Content)
parser=StrOutputParser()


phone_feedback1 = """
The NovaX Pro 12 is an absolute powerhouse in a sleek design. The 120Hz AMOLED display is stunning, 
making everything from streaming to scrolling buttery smooth. The camera system is top-tier, especially the night mode, 
which rivals professional DSLR results. Battery life easily lasts more than a day, and the fast charging is a 
game-changer — 0 to 80% in just 30 minutes! The UI is clean, responsive, and free from bloatware. 
Overall, it's a flagship experience at a competitive price.
"""

phone_feedback2 = """
The Xento M5 is a big disappointment. Despite all the hype, the phone feels laggy even during basic tasks. 
The camera is mediocre at best, producing grainy photos even in decent lighting. The battery drains quickly and the 
phone heats up after 20 minutes of use. On top of that, the fingerprint sensor is inconsistent and frustrating. 
For this price, there are far better options on the market.
"""

phone_feedback3 = """
The Zephyr Lite is a decent mid-range phone with a few trade-offs. The performance is fine for everyday use, 
but it’s not built for heavy gaming. The display is sharp, though the refresh rate is only 60Hz. 
The camera takes good photos in daylight but struggles in low light. Battery life is average, 
and it comes with minimal software bloat. It’s not exceptional, but it gets the job done.
"""
phone_feedback4 = """
This phone? Nah fam. 🚫💀
I turned it on and it already needed a break. Lagging like it’s 2012. Camera be making me look like a Minecraft character. 
Battery dies faster than my social life on Mondays. And don’t even try gaming on this — unless you like pain. 😤
"""
from pydantic import BaseModel
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field
class Sentiment(BaseModel):
    sentiment: Literal["Pos", "Neg", "U"]= Field(
        description="Sentiment of the feedback. Pos for Positive, Neg for Negative, U for Unclear"
    )


parser2=PydanticOutputParser(pydantic_object=Sentiment)


chain= prompt | modelGemini | parser2


response=chain.invoke({
    "content": phone_feedback4,
    "format_instructions": parser2.get_format_instructions(),
})

print("Feedback Analysis for Phone 1:")
print(response)
