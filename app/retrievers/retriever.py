from langchain_community.vectorstores import FAISS
def retriever(vector_store : FAISS): 
    retri = vector_store.as_retriever(
        search_type="similarity_score_threshold", 
        search_kwargs = {
            "k" : 5, 
            "score_threshold": 0.2 
        }
    )
    return retri