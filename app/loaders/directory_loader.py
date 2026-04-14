# In py 3.3, we have implicit Python packages. You can act like with the folder in the root 
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader 
from app.utils.definitions import get_root_dir 

ROOT_DIR = get_root_dir() 
print("This is root dir", ROOT_DIR) 

def directory_loader(): 
    print(ROOT_DIR)
    loader = DirectoryLoader(
        path = str(f"{ROOT_DIR}/datas"), 
        glob = "**/*.pdf", 
        loader_cls=PyPDFLoader, # Unstructured File Loader: Doc du lieu tu nhieu loai file khac nhau 
        show_progress=True, 
        use_multithreading=True 
    )
    docs = loader.load() 
    print(len(docs)) 
