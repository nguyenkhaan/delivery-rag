from langchain_text_splitters import RecursiveCharacterTextSplitter
MARKDOWN_SEPARATORS = [
    r"\n#{1,6} ",        # headings (# to ######)
    r"```\n",            # fenced code block start
    r"\n\*\*\*+\n",      # *** horizontal rules
    r"\n---+\n",         # --- horizontal rules
    r"\n___+\n",         # ___ horizontal rules
    r"\n\n",             # paragraph breaks
    r"\n",               # line breaks
    r" ",                # spaces
    r""                  # fallback to character level
]  
def recursive_splitter(docs): 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200, #So luong ki tu 
        chunk_overlap=200, 
        add_start_index=True, #Luu lai vi tri bat dau cua moi chunk -> Co the giup chatbot chi ra nguon thong tin da dua vao 
        strip_whitespace=True, #Loai bo ki tu trang o dau va cuoi cua doan chunk
        separators=MARKDOWN_SEPARATORS #Giup chatbot biet duoc dau la cac ki tu co the giup bat dau 1 chunk 
    ) 
    splits = text_splitter.split_documents(docs) 
    return splits
    