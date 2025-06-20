from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
# Define examples for the few-shot prompt
examples = [
    {
        "question": "Who lived longer, Steve Jobs or Einstein?",
        "answer": """Does this question require additional questions: Yes.
Additional Question: At what age did Steve Jobs die?
Intermediate Answer: Steve Jobs died at the age of 56.
Additional Question: At what age did Einstein die?
Intermediate Answer: Einstein died at the age of 76.
The final answer is: Einstein
""",
    },
    {
        "question": "When was the founder of Naver born?",
        "answer": """Does this question require additional questions: Yes.
Additional Question: Who is the founder of Naver?
Intermediate Answer: Naver was founded by Lee Hae-jin.
Additional Question: When was Lee Hae-jin born?
Intermediate Answer: Lee Hae-jin was born on June 22, 1967.
The final answer is: June 22, 1967
""",
    },
    {
        "question": "Who was the reigning king when Yulgok Yi's mother was born?",
        "answer": """Does this question require additional questions: Yes.
Additional Question: Who is Yulgok Yi's mother?
Intermediate Answer: Yulgok Yi's mother is Shin Saimdang.
Additional Question: When was Shin Saimdang born?
Intermediate Answer: Shin Saimdang was born in 1504.
Additional Question: Who was the king of Joseon in 1504?
Intermediate Answer: The king of Joseon in 1504 was Yeonsangun.
The final answer is: Yeonsangun
""",
    },
    {
        "question": "Are the directors of Oldboy and Parasite from the same country?",
        "answer": """Does this question require additional questions: Yes.
Additional Question: Who is the director of Oldboy?
Intermediate Answer: The director of Oldboy is Park Chan-wook.
Additional Question: Which country is Park Chan-wook from?
Intermediate Answer: Park Chan-wook is from South Korea.
Additional Question: Who is the director of Parasite?
Intermediate Answer: The director of Parasite is Bong Joon-ho.
Additional Question: Which country is Bong Joon-ho from?
Intermediate Answer: Bong Joon-ho is from South Korea.
The final answer is: Yes
""",
    },
]
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)

# Create an example prompt template
example_prompt = PromptTemplate.from_template(
    "Question:\n{question}\nAnswer:\n{answer}"
)

# Print the first formatted example
# print(example_prompt.format(**examples[0]))

# Initialize the FewShotPromptTemplate
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:\n{question}\nAnswer:",
    input_variables=["question"],
)

# Example question
question = "How old was Bill Gates when Google was founded?"
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)

# Generate the final prompt
final_prompt = few_shot_prompt.format(question=question)
# print(final_prompt)

response = model.predict(final_prompt)
print(response)