import os 
from langchain_mistralai import MistralAIEmbeddings 

MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY') 
def mistral_embeddings(): 
    embeddings = MistralAIEmbeddings(
        model = 'mistral-embed', 
        api_key=MISTRAL_API_KEY
    )
    return embeddings