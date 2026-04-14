# 🍕 Food Delivery RAG System

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Core-00A67E?logo=langchain)](https://python.langchain.com/)
[![Mistral AI](https://img.shields.io/badge/Mistral-AI-FF8C00)](https://mistral.ai/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-3776AB)](https://faiss.ai/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📌 Introduction

A **Retrieval-Augmented Generation (RAG)** system for food delivery services built with LangChain, Mistral AI, and FAISS. This system retrieves relevant information from your document database and generates accurate, citation-focused responses using a large language model.

### Key Features
- 📄 **PDF Document Loading**: Automatically loads and processes PDF files from your data directory
- 🔍 **Semantic Search**: Uses vector embeddings to find relevant documents
- 🧠 **Citation-Focused**: Provides answers only based on available context with source citations
- ⚡ **Efficient Retrieval**: Leverages FAISS for fast vector similarity search
- 🛡️ **Strict Mode**: Never uses outside knowledge - strictly adheres to provided documents

---

## 📁 Folder Structure

```
rag/
├── app/
│   ├── agent/
│   │   └── chatbot.py              # LLM initialization (Mistral AI)
│   │
│   ├── embeddings/
│   │   └── mistral_embeddings.py   # Embedding model for vectorization
│   │
│   ├── loaders/
│   │   └── directory_loader.py     # PDF document loader
│   │
│   ├── retrievers/
│   │   └── retriever.py            # Vector store retriever configuration
│   │
│   ├── stores/
│   │   └── vector_store.py         # FAISS vector store setup
│   │
│   ├── textsplitters/
│   │   └── recursive_splitter.py   # Document chunking strategy
│   │
│   ├── utils/
│   │   └── definitions.py          # Utility functions and path definitions
│   │
│   └── services/                   # Reserved for additional services
│
├── api/                            # API endpoints (if applicable)
├── datas/                          # PDF documents folder
├── main.py                         # Application entry point
├── requirements.txt                # Project dependencies
├── .env                            # Environment variables (MISTRAL_API_KEY)
└── README.md                       # This file
```

---

## 🔄 RAG System Flow

```
┌─────────────────┐
│  PDF Documents  │
│  (in /datas/)   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 1. Document Loading             │
│    DirectoryLoader (PyPDFLoader)│
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 2. Text Splitting               │
│    RecursiveCharacterSplitter   │
│    (Break into chunks)          │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 3. Embedding Generation         │
│    Mistral Embeddings           │
│    (Convert to vectors)         │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 4. Vector Store                 │
│    FAISS (Similarity Search)    │
└────────┬────────────────────────┘
         │
    ┌────┴─────┐
    │           │
┌───▼────┐  ┌──▼────────────────┐
│Question│  │ 5. Document       │
│ Input  │  │    Retrieval      │
└───┬────┘  │ (Top-K similar)   │
    │       └──┬─────────────────┘
    │          │
    └──────┬───┘
           │
           ▼
┌─────────────────────────────────┐
│ 6. LLM Processing               │
│    Mistral-Small                │
│    (Generate answer with context)
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 7. Response Output              │
│    Parsed & Citations           │
└─────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Mistral API Key ([Get one here](https://console.mistral.ai/))
- Virtual environment

### Installation

1. **Clone the repository**
```bash
git clone <your-repo>
cd rag
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
echo "MISTRAL_API_KEY=your_api_key_here" > .env
```

### Running the RAG System

1. **Add your PDF documents to the `datas/` folder**

2. **Run the application**
```bash
python -m main
```

3. **Enter your question when prompted**
```
Your Question: What restaurants deliver to my area?
```

4. **Get your answer with citations**
```
Based on the provided documents, [answer from context]
(source: document_name.pdf)
```

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `langchain-core` | Core LLM framework |
| `langchain-community` | Community tools & integrations |
| `langchain-mistralai` | Mistral AI integration |
| `langchain-text-splitters` | Document chunking utilities |
| `faiss-cpu` | Vector database for similarity search |
| `pypdf` | PDF parsing and reading |
| `python-dotenv` | Environment variable management |

---

## ⚙️ Configuration

### Environment Variables
Set these in your `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

### Adjustable Parameters

**In `main.py`:**
- `temperature=0` - Model determinism (0 = strict, 1 = creative)
- `max_retries=2` - API retry attempts
- `model='mistral-small'` - LLM model selection

**In `app/retrievers/retriever.py`:**
- `k=5` - Number of documents to retrieve
- `score_threshold=0.2` - Minimum relevance score (0-1)

---

## 💡 How It Works

1. **Loading**: PDF files are automatically loaded from `/datas/` directory
2. **Splitting**: Documents are split into manageable chunks (context preservation)
3. **Embedding**: Each chunk is converted to a vector using Mistral embeddings
4. **Storage**: Vectors are stored in FAISS vector database
5. **Retrieval**: When a question is asked, similar chunks are retrieved
6. **Generation**: The LLM uses retrieved context to generate a response
7. **Output**: Response is parsed and citations are included

---

## 🔒 Safety Features

- **Citation-Only Mode**: Only answers questions based on provided documents
- **Fallback Response**: "I don't know based on the provided documents." for out-of-context questions
- **Zero External Knowledge**: No web searches or external data usage
- **Transparency**: Source documents are cited in responses

---

## 📝 Example Usage

```python
# Add your PDF files to /datas/ folder
# Run the application
python -m main

# Input
>>> Your question about the food delivery service

# Output
Based on the provided context:
[Generated answer with specific details]

(source: restaurants.pdf, page 2)
```

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `MISTRAL_API_KEY not found` | Check `.env` file exists and has valid API key |
| `No documents loaded` | Ensure PDF files are in `/datas/` folder |
| `Vector store error` | Clear `venv/` and reinstall: `pip install -r requirements.txt` |
| `Permission denied` | Use `chmod +x main.py` on Linux/Mac |

---

## 📚 Learn More

- [LangChain Documentation](https://python.langchain.com/)
- [Mistral AI API](https://docs.mistral.ai/)
- [FAISS Vector Search](https://faiss.ai/)
- [RAG Concepts](https://python.langchain.com/docs/use_cases/rag/)

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Author

Built with Cloudian ❤️ for efficient document retrieval and Q&A systems