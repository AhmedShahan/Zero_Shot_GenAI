import asyncio
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# Step 1: Prompt setup
prompt = PromptTemplate.from_template("Explain {topic}")
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.)


# Step 2: Combine prompt and model
chain = prompt | model

# Step 3: Define async function to call ainvoke
async def main():
    query = {"topic": "Artificial Intelligence"}  # Dictionary format is required
    response = await chain.ainvoke(query)
    print(response.content)  # For ChatOpenAI/Chat model
    # print(response)        # For non-chat models

# Step 4: Run the async function
asyncio.run(main())
