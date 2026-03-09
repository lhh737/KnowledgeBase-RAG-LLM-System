"""
基于Streamlit完成WEB网页上传服务

Streamlit ： 当WEB页面元素变化，则代码重新执行一遍，无法维护状态
"""
import streamlit as st
import time


from konwledge_base import KnowledgeBaseService


# 添加网页标题
st.title("知识库更新服务")

# file_uploader
uploader_file=st.file_uploader(
    "请上传TXT文件",
    type=['txt'],
    accept_multiple_files=False,   # False表示仅接受一个文件的上传
)

if "service" not in st.session_state:          # 会话状态字典，session_state本身也是字典
    st.session_state["service"]=KnowledgeBaseService()
# count=0
if uploader_file is not None:
    # 提取文件信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size /1024
    st.subheader(f"文件名:{file_name}")
    st.write(f"格式:{file_type}  | 大小:{file_size:.2f}KB")

    # get_value -> bytes -> decode("utf-8")
    text=uploader_file.getvalue().decode("utf-8")

    with st.spinner("载入知识库中。。。"):     # 在 spinner内的代码执行过程中，会有一个转圈动画，优化用户体验
        time.sleep(1)
        result= st.session_state["service"].upload_by_str(text,file_name)
        st.write(result)