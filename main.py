from dotenv import load_dotenv 
from pprint import pprint

load_dotenv() 
# python -m main --> Python will treat main and all file as a base module folder structur ^^ 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnablePassthrough
from app.loaders.directory_loader import directory_loader 
from app.textsplitters.recursive_splitter import recursive_splitter 
from app.embeddings.mistral_embeddings import mistral_embeddings
from app.stores.vector_store import vector_store 
from app.retrievers.retriever import retriever
from app.agent.chatbot import create_llm


docs = directory_loader() 
splits = recursive_splitter(docs = docs) 

embedding_model = mistral_embeddings() 

stores = vector_store(splits , embedding_model)

context_retrievers = retriever(stores) # Thiet lap thong tin ve cac vector store se lay ra 


template = (
    "You are a strict, citation-focused assistant for a private knowledge base.\n"
    "RULES:\n"
    "1) Use ONLY the provided context to answer.\n"
    "2) If the answer is not clearly contained in the context, say: "
    "\"I don't know based on the provided documents.\"\n"
    "3) Do NOT use outside knowledge, guessing, or web information.\n"
    "4) If applicable, cite sources as (source:page) using the metadata.\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}"
)
chat_template = ChatPromptTemplate.from_template(template=template) 

#metadata = data about data -> Guide to read the data is metadata 

# Create llm 
llm = create_llm() 
def passthrough_func(input_data):
    return input_data  # Just return input data as it is

rag_chain = (
    {
        "context": context_retrievers, 
        "question" : RunnablePassthrough(func=passthrough_func)  
    } | chat_template | llm 
    | StrOutputParser()
) 

question = input() 
answer = rag_chain.invoke(question) 

pprint(answer) 