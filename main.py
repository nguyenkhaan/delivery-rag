# python -m main --> Python will treat main and all file as a base module folder structur ^^ 
from app.loaders.directory_loader import directory_loader 
from app.textsplitters.recursive_splitter import recursive_splitter 
from app.embeddings.mistral_embeddings import mistral_embeddings
from app.stores.vector_store import vector_store 
from dotenv import load_dotenv 

load_dotenv() 

docs = directory_loader() 
splits = recursive_splitter(docs = docs) 

embedding_model = mistral_embeddings() 

stores = vector_store(splits , embedding_model)

#metadata = data about data -> Guide to read the data is metadata 