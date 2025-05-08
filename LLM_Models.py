## pip install langchain
import langchain 

## Check the version of langchain
# print(langchain.__version__)

### LLMS of openAI
## First load the 



from langchain_openai import OpenAI
from dotenv import load_dotenv  
load_dotenv()
# Initialize the LLM correctly
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

# Call the LLM
result = llm.invoke("What is the capital of France?")

print(result)


## pip install langchain-openai





