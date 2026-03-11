# KnowledgeBase-RAG-LLM-System

 **基于 Streamlit 的本地知识库上传 + RAG 智能客服** 的简单复现项目：
- 在网页端上传 `txt` 文件，自动切分并向量化写入 Chroma 向量库
> 文档持久化  
- 在网页端以聊天形式提问，通过 **RAG（检索增强生成）** 基于知识库内容进行回答
> 模型prompt再生成注入  
- 支持 **会话历史查看**，流式思维链输出
> 实现长时记忆，模型可根据历史信息回答，再续前缘
- 技术栈：Python / Streamlit / LangChain / Chroma / Embeddings / Qwen ChatModel

---

## ✨ 功能一览

### 1) 知识库更新服务（Upload）
- Streamlit 页面上传文件，显示基本格式
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

### 3) 效果预览（demo）
---
<!-- 智能客服示例图 -->
<div align="left">
  <img src="https://github.com/lhh737/KnowledgeBase-RAG-LLM-System/raw/master/chat_demo1.png" width="750" alt="智能客服聊天界面示例">
</div>


- 本地知识库预存了衣物尺码推荐表、材质维护、穿衣搭配....
- 对标电商（可自行更改符合个人需求）

---

<!-- 智能客服示例图 -->
<div align="left">
  <img src="https://github.com/lhh737/KnowledgeBase-RAG-LLM-System/raw/master/chat_demo2.png" width="750" alt="智能客服聊天界面示例">
</div>

- 缓存用户对话信息精确回答

---

## 🧩 项目结构（建议）

> 如果你现在文件名不完全一致也没关系，但建议逐步整理成这种清晰结构...

```text
KnowledgeBase-RAG-LLM-System/
├─ app_upload.py                # 知识库上传服务（Streamlit）
├─ app_chat.py                  # 智能客服（Streamlit）
├─ rag.py                       # RagService：组装 RAG chain
├─ vector_stores.py             # VectorStoreService：Chroma retriever 封装
├─ konwledge_base.py            # KnowledgeBaseService：上传、切分、写库、去重
├─ file_history_store.py        # FileChatMessageHistory：会话历史落盘
├─ config_data.py               # 项目配置（模型名、路径、chunk 参数等）
|
├─ requirements.txt             # 依赖
|
├─ chroma_db/                   # Chroma 本地持久化目录（运行后生成）
├─ chat_history/                # 聊天历史目录（运行后生成）
└─ md5.text                     # 已入库内容的 md5 记录（运行后生成）

```
---
## ✅ 环境准备


### 1) 安装依赖
> pip install -r requirements.txt

- 终端运行，建议虚拟环境加载，自行添加清华镜像源加速
---

## ⚙️ 配置说明

- config_data.py 中包含核心配置，可手动修改模型配置、chunk大小...
- 默认text-embedding-v4及qwen3-max
- 注意，DashScope/通义千问相关的 API Key（例如 DASHSCOPE_API_KEY）需要系统环境变量中先行配置。

---

## 🚀 快速运行
### 1) 启动知识库上传服务
> streamlit run app_upload.py

- 打开页面后上传 .txt 文件即可写入向量库。

### 2) 启动智能客服（RAG Chat）
> streamlit run app_chat.py

- 输入问题后，会先检索知识库，再结合检索内容由模型生成回答（支持流式输出 | 历史记忆)

---

## 🛠 常见问题

- Q1：为什么我上传文件后，聊天回答仍然像“没检索到资料”？

- A: 向量库持久化目录不一致（upload 与 chat 指向不同 persist_directory）

- A: collection_name 不一致
- A: 未根据路径，创建data来保存文件

- Q2：为什么我上传文件后，输出对话却迟迟不显示？

- A: 检索参数 k 太小，默认小于5，修改chunk大小

- Q3: 为什么？.....
- A: 需修改之处都是数据输出处，自行配置成本地环境即可！

---
## ✨ 优化方向（仅供参考）
- 采用深度rerank，可自行添加langchain框架中的EGE rerank模块，回答更精准
- 页面优化：streamlit内置许多功能，可按需丰富UI
- 思维链 -> 思维树 ？
- 单模型 -> 多模型 ？ 比如豆包的多层推理架构，多模型混合输出？
- TXT文本-> 多模态 ？
- Chroma -> FAISS ?  这里采用轻量Chroma适合个人复现，FAISS的高效检索则适配企业
- 待定...
- 总之，这是一个基础但延展性很好的RAG项目,简单扩展 -> 企业级RAG -> ( 添加功能插件) -> Agent -> AI产品

---

## 📄 License

- 本项目仅用于学习与交流，如需商用请自行完善安全与合规策略。
---

## 🙌 致谢

- **Black Horse** 
- Streamlit
- LangChain
- Chroma / chromadb
- Aliyun Bai / qwen
