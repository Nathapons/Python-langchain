import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()
api_keys = os.getenv("API_KEYS")
print(f'{api_keys=}')
if api_keys is None:
    raise ValueError("API_KEYS environment variable not set")

# Initialize the ChatOpenAI model with the provided API key
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_keys, temperature=0)

# Print the response from the model
try:
    response = llm.invoke("เมืืองหลวงของประเทศไทยคืออะไร")
    print(response.content)
except Exception as e:
    print(f"Error occurred: {e}")
    response = None
