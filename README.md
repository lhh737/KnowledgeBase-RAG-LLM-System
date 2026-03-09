<p align="center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lhh737/KnowledgeBase-RAG-LLM-System/main/docs/assets/logo-light.png">
        <img src="https://raw.githubusercontent.com/lhh737/KnowledgeBase-RAG-LLM-System/main/docs/assets/logo-dark.png" alt="KnowledgeBase-RAG-LLM-System" width="500">
    </picture>
</p>

<p align="center">
  <strong>本地知识库 + RAG 智能问答系统</strong>
</p>

<p align="center">
  <a href="https://github.com/lhh737/KnowledgeBase-RAG-LLM-System/actions/workflows/ci.yml?branch=main"><img src="https://img.shields.io/github/actions/workflow/status/lhh737/KnowledgeBase-RAG-LLM-System/ci.yml?branch=main&style=for-the-badge" alt="CI status"></a>
  <a href="https://github.com/lhh737/KnowledgeBase-RAG-LLM-System/releases"><img src="https://img.shields.io/github/v/release/lhh737/KnowledgeBase-RAG-LLM-System?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
  <a href="https://github.com/lhh737/KnowledgeBase-RAG-LLM-System/discussions"><img src="https://img.shields.io/github/discussions/lhh737/KnowledgeBase-RAG-LLM-System?style=for-the-badge" alt="Discussions"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
</p>

**KnowledgeBase-RAG-LLM-System** 是一个本地运行的个人 AI 知识库系统。
它允许用户上传 TXT 文件构建知识库，并在聊天界面中进行智能问答，支持多轮对话和流式输出。如果你想要一个本地、快速、始终在线的 RAG 问答系统，这就是它。

[仓库主页](https://github.com/lhh737/KnowledgeBase-RAG-LLM-System) · [文档](docs/README.md) · [愿景](VISION.md) · [快速开始](docs/getting-started.md) · [更新指南](docs/updating.md) · [展示](docs/showcase.md) · [FAQ](docs/faq.md) · [Docker](docs/docker.md)

首选设置：在终端运行启动向导 (`python setup.py`)。
向导将逐步引导你设置知识库、聊天界面、配置和依赖。CLI 向导是推荐路径，支持 **Windows、macOS 和 Linux**。
兼容 pip、poetry 或 conda。
新安装？从这里开始：[快速开始](docs/getting-started.md)

## 赞助商

| Alibaba Cloud                                                     | LangChain                                                         | Streamlit                                                         |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| [![Alibaba Cloud](docs/assets/sponsors/alibaba.svg)](https://www.aliyun.com/) | [![LangChain](docs/assets/sponsors/langchain.svg)](https://langchain.com/) | [![Streamlit](docs/assets/sponsors/streamlit.svg)](https://streamlit.io/) |

**模型支持（API）：**

- **[DashScope (阿里云)](https://dashscope.aliyun.com/)** (Embedding + Qwen 模型)

模型说明：虽然支持多种模型，但为获得最佳体验和更低的提示注入风险，请使用最新一代最强模型。详见 [配置](docs/configuration.md)。

## 模型（选择 + 认证）

- 模型配置 + CLI：[模型](docs/models.md)
- 认证轮换（API 密钥）+ 回退：[模型容错](docs/model-failover.md)

## 安装（推荐）

运行时：**Python ≥3.10**。

```bash
git clone https://github.com/lhh737/KnowledgeBase-RAG-LLM-System.git
cd KnowledgeBase-RAG-LLM-System

pip install -r requirements.txt
# 或: poetry install

python setup.py  # 运行向导安装依赖和配置

向导会安装必要的服务（如 Chroma 持久化），确保系统保持运行。

快速开始（TL;DR）

运行时：Python ≥3.10。

完整新手指南（认证、配置、界面）：快速开始

python setup.py  # 安装向导

streamlit run app_upload.py  # 启动知识库上传界面

# 上传 TXT 文件
# 示例：上传 "knowledge.txt" 并构建知识库

streamlit run app_chat.py  # 启动智能客服聊天界面

# 发送消息
python rag.py --input "公司的退货政策是什么？" --session "user_001"

升级？更新指南
（并运行 python doctor.py）。

开发通道

stable：标记发布 (vYYYY.M.D 或 vYYYY.M.D-<patch>)。

beta：预发布标签 (vYYYY.M.D-beta.N)。

dev：main 分支头部。

切换通道：git checkout stable|beta|dev。
详情：开发通道
。

从源代码（开发）

推荐使用 poetry 构建源代码。

git clone https://github.com/lhh737/KnowledgeBase-RAG-LLM-System.git
cd KnowledgeBase-RAG-LLM-System

poetry install
poetry run streamlit run app_upload.py  # 测试上传界面

# 开发循环（自动重载）
poetry run watch  # 监控变化

注意：poetry run 直接运行 Python。构建 dist/ 用于生产部署。

安全默认（访问控制）

系统连接真实知识库和聊天界面。将输入视为 不受信任输入。

完整安全指南：安全

默认行为：

上传去重 (md5_path): 使用 MD5 检查重复，避免重复存储。

会话隔离 (session_id): 每个用户独立会话，防止交叉污染。

公开输入需显式选择：设置 allow_open=True 并在配置中包含 "*"。

运行 python doctor.py 以检查风险/误配置。

亮点

本地知识库
 — 单控制平面，用于上传、分块、向量化。

多界面支持
 — 上传界面 + 聊天界面，支持 Streamlit Web。

多会话路由
 — 路由输入到隔离会话（工作区 + 每个会话）。

流式输出
 — 支持实时响应和多轮对话。

一流工具
 — 向量检索、Prompt 构建、历史存储。

配置向导
 — 捆绑/管理/工作区配置。

持久化
 — Chroma 向量库 + 文件历史。

Star History

我们构建的一切
核心平台

知识库服务
 与会话、配置、持久化和 Prompt 构建。

CLI 界面
: 上传、聊天、发送、向导和诊断。

RAG 运行时
 在 RPC 模式下，支持工具流和块流。

会话模型
: 主会话用于直接聊天、隔离、多轮支持。

媒体管道
: 文本处理、切分、MD5 去重、临时文件生命周期。

接口

接口
: 上传界面
 (Streamlit)、聊天界面
 (Streamlit)。

路由
: 提及门控、回复标签、每个界面分块和路由。

应用 + 服务

Streamlit 应用
: 上传 + 聊天控制平面、调试工具。

服务模式
: 系统运行 + 配置暴露。

工具 + 自动化

向量控制
: 专用 Chroma、检索、上传、配置。

历史存储
: 文件存储、会话管理。

配置 + 唤醒
; 钩子
。

技能平台
: 捆绑、管理和工作区技能 + 安装门控。

运行时 + 安全

路由
、重试策略
 和 流式/分块
。

存在
、指示器
 和 使用跟踪
。

模型
、容错
 和 会话修剪
。

安全
 和 故障排除
。

运维 + 打包

控制 UI
 + 聊天
 直接从服务提供。

Docker 服务
 或 隧道
 带令牌/密码认证。

Nix 模块
（即将推出）。

贡献者
<p align="center"> <a href="https://github.com/lhh737"><img src="https://avatars.githubusercontent.com/u/12345678?v=4&s=48" width="48" height="48" alt="lhh737" title="lhh737"/></a> <!-- 添加更多贡献者头像，如果有的话 --> </p> ```
