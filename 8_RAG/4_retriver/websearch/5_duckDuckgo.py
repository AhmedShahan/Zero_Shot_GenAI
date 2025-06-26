import json
from langchain_community.tools import DuckDuckGoSearchResults

# Initialize the DuckDuckGo search tool
ddg_search = DuckDuckGoSearchResults()

# Query
query = "Who is the CEO of Meta?"
results = ddg_search.invoke(query)

# Parse the results to JSON (if not already structured)
try:
    # If results is a string, convert it to JSON
    if isinstance(results, str):
        results_json = json.loads(results)
    else:
        results_json = results
    print("Full Search Results (JSON):", json.dumps(results_json, indent=2))
except json.JSONDecodeError:
    print("Error: Could not parse results as JSON. Raw output:", results)

# Alternative: Pretty-print if results is already a list of dictionaries
if isinstance(results, list):
    print("Full Search Results (List):", json.dumps(results, indent=2))