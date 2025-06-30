from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
import os

# Load environment variables
load_dotenv()

# Initialize the search tool
search_tool = TavilySearchResults()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Define a refined custom ReAct prompt
custom_react_prompt = PromptTemplate(
    input_variables=["input", "tools", "tool_names", "agent_scratchpad"],
    template="""Answer the following question as best as you can. You have access to the following tools: {tools}.
The tool names are: {tool_names}.

Use the following format strictly:

Question: {input}

Thought: [Your reasoning about how to answer the question]
Action: [The tool you will use, e.g., tavily_search_results_json]
Action Input: [The input to the tool]

[Tool Output: The result from the tool will be inserted here by the agent]

[... repeat Thought/Action/Action Input/Tool Output as needed ...]

Thought: [After processing tool output, reason about the next step or finalize the answer]
Final Answer: [Provide a detailed and structured response to the question. Include specific details such as bus operator names, ticket prices, schedules, and any other relevant information. If prices are in multiple currencies, clarify the currency. If there are multiple options, list them clearly in a structured format (e.g., bullet points or a table). If no specific details are available, explain why and suggest next steps.]

**Instructions**:
- Do not provide a Final Answer until you have gathered and processed all necessary information from the tools.
- If a tool provides insufficient information, consider performing another search or explain the limitation in the Final Answer.
- Ensure the response is concise, accurate, and structured, with clear details about bus operators, prices, and schedules.
- Always clarify the currency (e.g., BDT or USD) for prices.
- If schedules are unavailable, suggest checking official websites or booking platforms like Shohoz (www.shohoz.com), bdtickets (www.bdtickets.com), or busbd (www.busbd.com.bd).

Begin by reasoning about how to answer the question:

Thought: [Your initial reasoning]

{agent_scratchpad}
"""
)

# Create the ReAct agent with the custom prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=custom_react_prompt
)

# Create the agent executor with error handling
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True,
    return_intermediate_steps=True,
    handle_parsing_errors=True  # Enable error handling
)

# Define the query
query = "What are the buses to reach Dhaka to Chittagong with price"

# Execute the query
result = agent_executor.invoke({"input": query})

# Print the result
# print("Intermediate Steps:", result["intermediate_steps"])
print("Final Output:", result["output"])