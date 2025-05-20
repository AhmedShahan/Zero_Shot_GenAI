from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
load_dotenv()


model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.9
)

prompt="write down the summary of Attendtion All you Need Paper"
summary = model.invoke(prompt)
summary_content=summary.content

class StructuredSummary(TypedDict):
    title: Annotated[str, "Write down the title of the paper"]
    authors: Annotated[list[str], "Write down the authors' names in a list"]
    keywords: Annotated[list[str], "Write down the keywords of the paper in a list"]
    abstract: Annotated[str, "Write a short summary or abstract of the paper"]
    problem_statement: Annotated[str, "Describe the problem or research gap the paper addresses"]
    methodology: Annotated[str, "Explain the methods, models, or frameworks used in the paper"]
    results: Annotated[str, "Summarize the main results or findings of the paper"]
    conclusion: Annotated[str, "Write down the conclusion or takeaway from the paper"]
    future_work: Annotated[str, "Mention any suggested future directions or work"]
    citation: Annotated[str, "Provide the formatted citation (IEEE/APA/etc.) of the paper"]
    paper_link: Annotated[str, "Include the link or DOI of the paper"]

structured_model=model.with_structured_output(StructuredSummary)

### Chain
structured_response= structured_model.invoke(summary_content)

# Print all elements
print("Title:", structured_response.get("title", "N/A"))
print("Authors:", structured_response.get("authors", []))
print("Key Term:", structured_response.get("key_term", "N/A"))
print("Keywords:", structured_response.get("keywords", []))
print("Abstract:", structured_response.get("abstract", "N/A"))
print("Problem Statement:", structured_response.get("problem_statement", "N/A"))
print("Methodology:", structured_response.get("methodology", "N/A"))
print("Results:", structured_response.get("results", "N/A"))
print("Conclusion:", structured_response.get("conclusion", "N/A"))
print("Future Work:", structured_response.get("future_work", "N/A"))
print("Citation:", structured_response.get("citation", "N/A"))
print("Paper Link:", structured_response.get("paper_link", "N/A"))
