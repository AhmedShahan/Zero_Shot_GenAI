# from dotenv import load_dotenv
# import os
# from langchain_huggingface import HuggingFaceEndpoint

# load_dotenv()

# # Initialize the HuggingFace model
# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# # Get response
# response = llm.invoke("Tell me a joke about a cat.")

# # Print response
# print(response)




from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()

# Initialize the HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="togethercomputer/llama-2-7b-chat",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# Get response
response = llm.invoke("Tell me a joke about a cat.")

# Print response
print(response)