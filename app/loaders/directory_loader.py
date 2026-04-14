# In py 3.3, we have implicit Python packages. You can act like with the folder in the root 
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader 
from app.utils.definitions import get_root_dir 

ROOT_DIR = get_root_dir() 

def directory_loader(): 
    loader = DirectoryLoader(
        path = str(f"{ROOT_DIR}/datas"), 
        glob = "**/*.pdf", 
        loader_cls=PyPDFLoader, # Unstructured File Loader: Doc du lieu tu nhieu loai file khac nhau 
        show_progress=True, 
        use_multithreading=True 
    )
    docs = loader.load() 
    return docs 
