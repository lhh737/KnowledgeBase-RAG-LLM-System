<div align="center">

# KnowledgeBase RAG LLM System

**A lightweight local knowledge-base RAG system built with Streamlit, LangChain and Chroma**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Chroma](https://img.shields.io/badge/Chroma-0.5-F48C06?style=flat-square&logo=chroma&logoColor=white)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](./LICENSE)

[中文](README.md) | [English](README.en.md)

</div>

---

## Introduction

A lightweight, fully local **RAG (Retrieval-Augmented Generation)** project. Upload `.txt` documents, they are chunked and indexed automatically; then ask questions in a chat interface and get answers grounded in your own content.

- **Knowledge base upload** — upload `.txt` files from the browser, chunked and written to a Chroma vector store with MD5 deduplication
- **RAG Q&A** — a `Retrieval → Prompt → LLM → Output` chain with streaming output
- **Session handling** — message history is kept, enabling follow-up questions in context

> A clean starting point for learning RAG: readable structure, light dependencies, no GPU required. Swap in your own documents and it adapts to a real use case.

## Demo

<div align="center">
  <img src="./assets/chat_demo1.png" width="720" alt="Single-turn QA">
  <br>
  <em>Figure 1 · Single-turn question answering</em>
</div>

<br>

<div align="center">
  <img src="./assets/chat_demo2.png" width="720" alt="Follow-up question">
  <br>
  <em>Figure 2 · Follow-up question using conversation history</em>
</div>

The sample knowledge base ships with clothing size recommendations, fabric care and color-matching notes (see `assets/*.txt`) — modelled on an e-commerce support scenario. Replace them with your own domain text.

## Architecture

```
┌──────────────┐   upload .txt  ┌──────────────────┐   chunk + MD5 dedup
│  Streamlit   │ ────────────▶ │  KnowledgeBase   │ ──────────────┐
│  upload UI   │                │  (knowledge_base) │               │
└──────────────┘                └──────────────────┘               ▼
                                                          ┌────────────────┐
┌──────────────┐   user question ┌──────────────────┐        │  Chroma        │
│  Streamlit   │ ──────────────▶ │   RAG Chain      │ ─────▶ │  local vector  │
│  chat UI     │ ◀────────────── │     (rag.py)     │        │  store         │
└──────────────┘   streaming out └──────────────────┘        └────────────────┘
```

| Module | Description |
|--------|-------------|
| `app_upload.py` | Upload service (Streamlit page) |
| `app_chat.py` | Chat interface (Streamlit page) |
| `knowledge_base.py` | Document reading, chunking, indexing, MD5 dedup |
| `rag.py` | RAG chain assembly (retrieve → prompt → LLM → output) |
| `vector_stores.py` | Vector store wrapper with Chroma persistence |
| `file_history_store.py` | Conversation history (FileChatMessageHistory) |
| `config_data.py` | Model names, paths and chunking parameters |

## Quick Start

### Requirements

- Python ≥ 3.10
- A DashScope API key — request one from [Alibaba Cloud Model Studio](https://bailian.console.aliyun.com/)

### 1. Install dependencies

```bash
git clone https://github.com/lhh737/KnowledgeBase-RAG-LLM-System.git
cd KnowledgeBase-RAG-LLM-System

pip install -r requirements.txt
```

### 2. Configure the API key

```bash
# Linux / macOS
export DASHSCOPE_API_KEY="your-api-key"

# Windows (CMD)
set DASHSCOPE_API_KEY=your-api-key
```

### 3. Run

```bash
# Terminal 1 — upload service
streamlit run app_upload.py

# Terminal 2 — chat service
streamlit run app_chat.py
```

Then open **http://localhost:8501**

### 4. Workflow

1. Open the upload page, upload a `.txt` file — it is chunked and indexed automatically
2. Open the chat page, ask a question — the system retrieves relevant chunks first, then answers with the LLM

## Configuration

Core settings live in `config_data.py`:

| Setting | Default | Description |
|---------|---------|-------------|
| `embedding_model_name` | `text-embedding-v4` | Embedding model |
| `chat_model_name` | `qwen3-max` | Chat model |
| `chunk_size` / `chunk_overlap` | `1000` / `100` | Chunking granularity |
| `similarity_threshold` | `1` | Number of documents returned by retrieval |
| `persist_directory` | `./chroma_db` | Vector store persistence directory |

> ⚠️ Both services must point at the **same store directory and `collection_name`**, otherwise retrieval returns nothing.

## FAQ

<details>
<summary><b>Q: I uploaded a file but the assistant still can't find it.</b></summary>

- The upload and chat services point at different persistence directories
- `collection_name` differs between the two
- The document was not actually written to the local data directory
</details>

<details>
<summary><b>Q: Answers are slow or nothing is generated.</b></summary>

- Chunking or retrieval parameters (chunk size, top-k) need tuning
- The model API or network is slow
- The local vector store was not initialised correctly
</details>

<details>
<summary><b>Q: Path or configuration errors on startup.</b></summary>

Check `config_data.py` for model and path settings, confirm the data directory exists, and verify the API key is exported.
</details>

## Roadmap

A small but extensible RAG scaffold:

- **Better retrieval** — add a reranker (e.g. bge-reranker) to improve precision
- **More file types** — PDF / Markdown / Word via LangChain loaders
- **Reasoning** — CoT → ToT, multi-model output mixing
- **Storage** — Chroma (lightweight, ideal for reproduction) → FAISS / Milvus (high concurrency, production)
- **Productization** — enterprise RAG → plugins → agents → AI product

## License

MIT © [lhh737](https://github.com/lhh737)

## Acknowledgments

- [Streamlit](https://streamlit.io/) · [LangChain](https://www.langchain.com/) · [Chroma](https://www.trychroma.com/)
- [Alibaba Cloud Model Studio / Qwen](https://bailian.console.aliyun.com/)