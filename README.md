## Dependencies 
- langchain-core: Langchain main framework 
- langchain-community: Langchain tool 
- langchain-text-splitters
- faiss-cpu: vector database 
- unstrucured: parse file 
- pypdf: read pdf file 


## Folder structure 

langchain_app/
│
├── app/
│   ├── loaders/              
│   │   └── directory_loader.py
│   │
│   ├── retrievers/
│   ├── vectorstores/
│   ├── embeddings/
│   ├── chains/
│   ├── agents/
│   ├── tools/
│   ├── prompts/
│   ├── services/
│   └── config/
│
├── data/                     
│   ├── pdfs/
│   ├── docs/
│   └── restaurants/
│
├── api/
└── main.py