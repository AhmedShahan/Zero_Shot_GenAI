from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load the API key

# Initialize the Gemini model using LangChain
# Initialize the Gemini model using LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5
)

# Ask a question
query=[
    "Write a short story about a cat in a futuristic city.",
    "Describe a dog who became president in the year 3000.",
    "What would a coffee shop on Mars be like?",
    "Tell me a bedtime story involving a robot and a sunflower."
]
responses = llm.batch(query)
# print(response)

'''
content='Neon signs painted the rain-slicked streets of Neo-Kyoto in a kaleidoscope of electric blues and venomous greens.  Above, flying cars zipped between towering chrome skyscrapers, their engines a low hum that vibrated through the grimy alleyways.  Here, nestled in a discarded data-pod, lived Glitch.\n\nGlitch wasn\'t your average alley cat.  His fur, the color of burnt caramel, was speckled with bioluminescent algae, a quirk from his genetically modified ancestors. His eyes, a startling emerald green, glowed faintly in the dim light.  He was a survivor, a phantom flitting through the city\'s underbelly, a creature of shadows and discarded technology.\n\nTonight, Glitch was hungry.  The usual scraps around the noodle stall were gone.  He padded silently along the alley, his claws clicking on the metallic grating.  A sudden whirring sound made him freeze.  A drone, sleek and silver, hovered nearby, its camera lens focusing on him.\n\nGlitch knew these drones.  They were the city\'s sanitation bots, programmed to eliminate "unwanted elements."  He flattened himself against the wall, his bioluminescent fur camouflaging him against the neon glow.  The drone passed, its sensors apparently failing to detect him.\n\nHe continued his hunt, his senses sharp and alert.  He spotted a discarded energy bar, its foil wrapper slightly torn.  A feast!  He devoured it quickly, the synthetic sweetness a welcome change from the usual stale scraps.\n\nSuddenly, a high-pitched whine pierced the night.  A chase ensued.  A small, robotic dog, its circuits sparking erratically, was being pursued by a larger, more menacing security bot.  The dog, clearly malfunctioning, stumbled, its tiny metal legs buckling.\n\nGlitch, despite his own hunger, felt a surge of something akin to empathy.  He darted forward, distracting the security bot with a well-timed hiss and a swipe of his paw.  The robotic dog, seizing the opportunity, limped away into the darkness.\n\nGlitch watched it go, then turned and melted back into the shadows.  He was just a cat, a creature of instinct and survival, in a city of gleaming chrome and cold logic.  But tonight, he had done something more.  He had shown a flicker of compassion in a world that had forgotten how to feel.  And as he settled down in his data-pod, the faint glow of his fur a silent testament to his existence, he knew he would survive another night in Neo-Kyoto.' additional_kwargs={} response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'model_name': 'gemini-1.5-flash', 'safety_ratings': []} id='run--5d259ced-5486-4003-988a-8390435eca31-0'

'''
# print(response)
for response in responses:
    print(response.content)
    print("*"*50)