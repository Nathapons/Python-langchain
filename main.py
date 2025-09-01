import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("API_KEYS environment variable not set")

# Initialize the ChatOpenAI model with the provided API key
# temperature is set to 0 for deterministic responses
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key, temperature=0)

# Create a prompt template for translating country names to English
prompt = ChatPromptTemplate.from_template([
    ("system", "คุณเป็นผู้เชี่ยวชาญทางด้าน {expertise}"),
    ("human", "อธิบายเกี่ยวกับ {topic} ให้เข้าใจง่ายๆ ใน {word} ประโยค"),
])

# Create chain by combining prompt and model
chain = prompt | llm

# Print the response from the model
try:
    response = chain.invoke({"expertise": "ประวัติศาสตร์", "topic": "สงครามโลกครั้งที่ 2", "word": 3})
    print(response.content)
except Exception as e:
    print(f"Error occurred: {e}")
    response = None
