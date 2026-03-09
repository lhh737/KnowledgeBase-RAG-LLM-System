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

## ✅ 环境准备
1) Python 版本

建议：Python 3.10+

2) 安装依赖
pip install -r requirements.txt

如果你还没有 requirements.txt，可以先按你项目实际依赖补齐（至少包含）：

streamlit

langchain

langchain-core

langchain-community

langchain-chroma

chromadb

⚙️ 配置说明

在 config_data.py 中包含核心配置，例如（示例含义）：

向量库

collection_name="rag"

persist_directory="./chroma_db"

文本切分

chunk_size=1000

chunk_overlap=100

separators=[... ]

max_spliter_char_number=1000

检索

similarity_threshold=1（返回文档数量 k）

模型

embedding_model_name="text-embedding-v4"

chat_model_name="qwen3-max"

会话

session_config = {"configurable": {"session_id": "user_001"}}

注意：DashScope/通义千问相关的 Key（例如 DASHSCOPE_API_KEY）通常需要你在系统环境变量中配置。
具体以你本地 SDK 要求为准。

🚀 快速运行
1) 启动知识库上传服务
streamlit run app_upload.py

打开页面后上传 .txt 文件即可写入向量库。

2) 启动智能客服（RAG Chat）
streamlit run app_chat.py

输入问题后，会先检索知识库，再结合检索内容由模型生成回答（支持流式输出）。

📝 使用流程

先运行 上传服务，上传你的 .txt 文档（构建知识库）

再运行 智能客服，对知识库内容提问

系统会把对话历史保存到本地 ./chat_history/，不同 session_id 对应不同文件

🔍 关键实现点

Streamlit 状态管理：使用 st.session_state 缓存对象，避免每次交互重建服务造成性能浪费

MD5 去重入库：同样内容不会重复向量化与写库

本地持久化：

Chroma：persist_directory

Chat History：./chat_history/<session_id>

链路（概念流程）：

用户输入

Retriever 检索相关片段

Prompt 拼接（context + history + input）

LLM 生成

输出（支持 stream）

🛠 常见问题
Q1：Streamlit 每次交互都会重跑，怎么保持对象不丢？

A：用 st.session_state 存对象（你项目里已使用），例如：

st.session_state["service"] = KnowledgeBaseService()

st.session_state["rag"] = RagService()

Q2：为什么我上传文件后，聊天回答仍然像“没检索到资料”？

可能原因：

向量库持久化目录不一致（upload 与 chat 指向不同 persist_directory）

collection_name 不一致

你上传的文本过短/被切分配置影响

检索参数 k 太小（你配置里叫 similarity_threshold，但实际是返回数量）

Q3：similarity_threshold 这个名字看起来像阈值？

A：在你当前代码里它用于 search_kwargs={"k": ...}，实际含义是 返回 top-k 文档数量。
建议后续把变量名改为 top_k 更直观。

📌 Git 使用小提示（你当前仓库已设置远程）

你已经执行过类似命令：

git remote set-url origin git@github.com:lhh737/KnowledgeBase-RAG-LLM-System.git

后续常用流程：

git add .
git commit -m "update"
git push
📄 License

本项目仅用于学习与交流，如需商用请自行完善安全与合规策略。

🙌 致谢

Streamlit

LangChain

Chroma / chromadb

DashScope / 通义千问
