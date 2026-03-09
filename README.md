#  KnowledgeBase-RAG-LLM-System

**本地知识库智能问答系统**  
基于 Streamlit + LangChain + Chroma + 通义千问 的完整 RAG 应用  
用户上传 TXT 即可构建知识库，通过聊天界面智能问答。

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/langchain-%231C3C3C.svg?style=for-the-badge&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## ✨ 项目特色
- 📤 **知识库上传**：TXT 文件自动分块、向量化、MD5 去重，避免重复存储  
- 💬 **智能客服**：RAG 检索增强生成，支持多轮对话 + 流式输出  
- 🗄️ **Chroma 向量库**：本地持久化，支持语义搜索  
- 🔄 **对话记忆**：文件存储历史记录，跨会话保留  
- 🚀 **纯本地部署**：无需服务器，简单两行命令启动  

---

## 🚀 快速开始
1. **克隆仓库**  
   ```bash
   git clone https://github.com/lhh737/KnowledgeBase-RAG-LLM-System.git
   cd KnowledgeBase-RAG-LLM-System

安装依赖（推荐虚拟环境）

pip install -r requirements.txt

设置 API Key
在终端执行（或写入 .env）：

export DASHSCOPE_API_KEY=你的密钥（从阿里云 DashScope 控制台获取）

运行项目

知识库上传界面：streamlit run app_upload.py

智能客服聊天界面：streamlit run app_chat.py
浏览器打开 http://localhost:8501

📁 项目结构
KnowledgeBase-RAG-LLM-System/
├── app_upload.py          # 知识库上传 Web 界面
├── app_chat.py            # 智能客服聊天界面
├── knowledge_base.py      # 知识库服务（MD5 + Chroma）
├── rag.py                 # RAG 核心链路
├── vector_stores.py       # 向量检索服务
├── file_history_store.py  # 对话历史文件存储
├── config_data.py         # 配置（chunk_size、模型名等）
├── chroma_db/             # 向量数据库（自动生成）
├── chat_history/          # 聊天记录（自动生成）
├── md5.txt                # 文档去重记录
└── requirements.txt       # 依赖列表
🛠️ 技术栈
技术	用途
Streamlit	Web 前端界面
LangChain	RAG 链路、Prompt、Retriever
Chroma	本地向量数据库
DashScopeEmbeddings	文本向量化
ChatTongyi (Qwen)	大语言模型 + 流式输出
RecursiveCharacterTextSplitter	智能文本分块
🔧 如何工作

上传 TXT → 切分文本 → MD5 去重 → 存入 Chroma

用户提问 → 向量检索相关片段 → 构建 Prompt → 通义千问生成答案

支持对话历史记忆与流式实时输出

示例 Prompt（内置）：
“以我提供的参考资料为主，简洁专业地回答。参考资料：{context}”

📌 项目亮点

完整 RAG 实现，适合 LLM 入门学习

去重 + 持久化，实用性强

两个独立 Streamlit 页面，体验流畅

🔮 TODO

 支持 PDF / Word 上传

 多用户会话管理

 文档管理界面

 Docker 一键部署

作者：lhh737

如果项目对你有帮助，欢迎 Star ⭐ 支持！
