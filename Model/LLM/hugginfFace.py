import os
import requests

# Get your Hugging Face API token
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")  # Make sure this is set in your environment

# Choose a model
model_id = "google/gemma-7b-it"  # You can change this to any model available on Hugging Face

# API endpoint
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

# Set headers with your API token
headers = {"Authorization": f"Bearer {api_token}"}

# Function to query the model
def query_model(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7,
            "return_full_text": False
        }
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
prompt = "What is the capital of Bangladesh?"
result = query_model(prompt)
print(result)