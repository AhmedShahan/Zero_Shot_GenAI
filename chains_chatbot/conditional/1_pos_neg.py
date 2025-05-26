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
    ('human', "Analyze the feedback and return the Positive or Negative Feedback for the following content {content} and feedback. If the feedback is positive, return 'Positive'. If the feedback is negative, return 'Negative'.")
]


prompt=ChatPromptTemplate.from_messages(Message_Content)
parser=StrOutputParser()

chain= prompt | modelGemini | parser

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


response=chain.invoke({
    "content": phone_feedback2
})
print("Feedback Analysis for Phone 1:")
print(response)
