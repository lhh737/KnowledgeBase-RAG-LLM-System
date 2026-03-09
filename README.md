# KnowledgeBase-RAG-LLM-System

一个基于 **Streamlit + LangChain + Chroma + 通义千问** 的本地知识库问答系统。  
支持 **TXT 文件上传入库、向量检索、对话记忆、多轮问答**，可用于快速搭建一个轻量级的 RAG（Retrieval-Augmented Generation，检索增强生成）应用。

---

## 项目简介

这个项目实现了一个简单完整的知识库问答流程：

- 使用 **Streamlit** 搭建 Web 页面
- 上传 **TXT 文件** 到本地知识库
- 对文本进行切分、向量化并存入 **Chroma**
- 用户在聊天页面提问时，系统先检索知识库相关内容
- 再结合 **历史对话记录**，调用大模型生成回答

适合学习和实践以下方向：

- RAG 基础项目搭建
- LangChain 链式调用
- 向量数据库接入
- Streamlit 快速开发 AI Web 应用
- 多轮对话与历史消息管理

---

## 功能特性

- **知识库上传**
  - 支持上传 `.txt` 文件
  - 自动读取文本内容并写入知识库
  - 使用 MD5 去重，避免重复入库

- **文本切分**
  - 基于 `RecursiveCharacterTextSplitter`
  - 支持按段落、标点、空格等多级分割文本

- **向量检索**
  - 使用 `DashScopeEmbeddings`
  - 向量数据持久化到本地 `Chroma`

- **智能问答**
  - 基于知识库内容进行语义检索
  - 调用大模型生成更贴合上下文的回答

- **对话记忆**
  - 历史消息保存到本地文件
  - 支持多轮连续问答

- **Web 可视化交互**
  - 基于 Streamlit 的简洁页面
  - 包含文件上传页与聊天页

---

## 项目结构

```bash
KnowledgeBase-RAG-LLM-System/
│
├── app_upload.py              # 知识库上传页面（示意名称）
├── app_chat.py                # 智能客服聊天页面（示意名称）
├── config_data.py             # 项目配置
├── konwledge_base.py          # 知识库写入服务
├── rag.py                     # RAG 核心服务
├── vector_stores.py           # 向量库检索服务
├── file_history_store.py      # 本地历史消息存储
│
├── chroma_db/                 # Chroma 本地向量数据库
├── chat_history/              # 对话历史记录目录
├── md5.text                   # 已入库文本 MD5 记录
│
└── README.md
