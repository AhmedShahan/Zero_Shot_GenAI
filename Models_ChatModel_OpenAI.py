from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo",  # ✅ this is a valid chat model
    temperature=0.9
)

result = model.invoke("What is the capital of Bangladesh?")
print(result)
'''
content='The capital of Bangladesh is Dhaka.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 14, 'total_tokens': 23, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-BUozEM236gwngmueTMpURIHxdJRr6', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--fe4220bb-92c1-4301-b5ce-fd153341cc9a-0' usage_metadata={'input_tokens': 14, 'output_tokens': 9, 'total_tokens': 23, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
Instead of just answer there a lot of information
'''

print(result.content)