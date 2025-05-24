'''
🔧 Idea: "Automated Blog Post Generator from a Topic"
This app will:

Take a topic input from the user.

Generate an outline of the blog.

Expand each outline point into a detailed paragraph.

Summarize the blog post at the end.

You can chain multiple LLMs (or just reuse one) to perform these tasks in sequence.


          [User Input]
               │
               ▼
   ┌───────────────────────────┐
   │ Step 1: Generate Outline  │ ← (LLM 1)
   └───────────────────────────┘
               │
               ▼
   ┌───────────────────────────┐
   │ Step 2: Expand Sections   │ ← (LLM 2)
   └───────────────────────────┘
               │
               ▼
   ┌───────────────────────────┐
   │ Step 3: Summarize Blog    │ ← (LLM 3)
   └───────────────────────────┘
               │
               ▼
         [Final Output]

User will enter the Topic
Select the Agents with temperature
One by One response Generation

terminal Based app will be created to take user input and display the output in a structured format.
'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()


print("Agent Based Sequencial Content Generation ")
print("Select the Agent Outline Generation")
agents=['gemini-1.5-flash', 'command-r-plus', 'gemma3:latest', 'deepseek-r1:latest', 'llama3.2:1b']
for i, agent in enumerate(agents, start=1):
    print(f"{i}. {agent}")
agent_choice = int(input("Enter the number corresponding to your choice: ")) - 1
print(f"You selected: {agents[agent_choice]}")

