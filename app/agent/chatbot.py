import os 
from langchain_mistralai import ChatMistralAI
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY') 

def create_llm(): 
    llm = ChatMistralAI(
        model = 'mistral-medium', 
        temperature=0,  # Muc do ngau nhien trong cau tra loi cua mo hinh 
        max_retries=2,
        api_key=MISTRAL_API_KEY 
    )
    return llm 