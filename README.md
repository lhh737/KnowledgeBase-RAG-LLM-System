# KnowledgeBase-RAG-LLM-System

一个 **基于 Streamlit 的知识库上传 + RAG 智能客服** 的可简单复现项目：  
- 在网页端上传 `.txt` 文件，自动切分并向量化写入 Chroma 向量库  
- 在网页端以聊天形式提问，通过 **RAG（检索增强生成）** 基于知识库内容进行回答  
- 支持 **会话历史落盘**（文件方式保存），让对话可持续

> 技术栈：Streamlit / LangChain / Chroma / DashScope Embeddings（text-embedding-v4）/ 通义千问 ChatTongyi（qwen3-max）

---

## ✨ 功能一览

### 1) 知识库更新服务（Upload）
- Streamlit 页面上传 `.txt`
- 自动读取文本内容
- 根据配置进行分段（RecursiveCharacterTextSplitter）
- 写入 Chroma 向量库（本地持久化）
- 使用 **MD5 去重**：相同内容不重复入库

### 2) 智能客服（RAG Chat）
- Streamlit Chat UI
- 显示历史消息（session_state）
- LangChain 链式调用：`Retrieval -> Prompt -> LLM -> Output`
- 支持 **流式输出**
- 支持 **消息历史文件存储**（FileChatMessageHistory）

---

## 🧩 项目结构（建议）

> 如果你现在文件名不完全一致也没关系，但建议逐步整理成这种清晰结构

```text
KnowledgeBase-RAG-LLM-System/
├─ app_upload.py                # 知识库上传服务（Streamlit）
├─ app_chat.py                  # 智能客服（Streamlit）
├─ rag.py                       # RagService：组装 RAG chain
├─ vector_stores.py             # VectorStoreService：Chroma retriever 封装
├─ konwledge_base.py            # KnowledgeBaseService：上传、切分、写库、去重
├─ file_history_store.py        # FileChatMessageHistory：会话历史落盘
├─ config_data.py               # 项目配置（模型名、路径、chunk 参数等）
├─ requirements.txt             # 依赖
├─ chroma_db/                   # Chroma 本地持久化目录（运行后生成）
├─ chat_history/                # 聊天历史目录（运行后生成）
└─ md5.text                     # 已入库内容的 md5 记录（运行后生成）
