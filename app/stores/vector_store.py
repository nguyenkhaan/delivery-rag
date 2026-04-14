from langchain_community.vectorstores import FAISS 
from langchain_community.vectorstores.utils import DistanceStrategy

def vector_store(chunks , model): 
    vector_stores = FAISS.from_documents(
        documents=chunks, 
        embedding = model, 
        distance_strategy = DistanceStrategy.COSINE
    )
    return vector_stores 