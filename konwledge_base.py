"""
知识库
"""
import os
import  config_data as config
import  hashlib
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime

def check_md5(md5_str:str):
    """检查传入的MD5字符串是否已经被处理过了
            return False未处理，True已处理
    """
    if not os.path.exists(config.md5_path):
        # if 进入表示文件不存在，表示没有处理过这个MD5
        open(config.md5_path,'w',encoding='utf-8').close()
        return False
    else:
        for line in open(config.md5_path,'r',encoding='utf-8').readlines():
            line=line.strip()   # 处理字符串前后的空格和回车
            if line == md5_str:
                return True     # 已处理过
        return False

def save_md5(md5_str:str):
    """将传入的md5字符串，记录到文件内保存"""
    with open(config.md5_path,'a',encoding="utf-8")as f:
        f.write(md5_str + '\n')

def get_string_md5(input_str:str ,encoding='utf-8'):
    """将出传入的字符串转换为md5字符串"""

    # 将字符串转换为bytes字节数组
    str_bytes = input_str.encode(encoding=encoding)

    # 创建md5 对象
    md5_obj =hashlib.md5()      # 得到md5对象
    md5_obj.update(str_bytes)   # 更新内容（传入即将要转换的字节数组）
    md5_hex=md5_obj.hexdigest() # 得到md5的十六进制字符串

    return md5_hex


class KnowledgeBaseService(object):
    def __init__(self):
        # 如果文件夹不存在则创建，如果存在则跳过
        os.makedirs(config.persist_directory,exist_ok=True)

        self.chroma=Chroma(          # 向量存储的示例 Chroma向量库对象
            collection_name=config.collection_name,      #数据库表名
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory,   #数据库本地存储文件夹
        )      # 向量存储的实例，Chroma向量库对象
        self.spliter=RecursiveCharacterTextSplitter(  # 文本分割器的对象
            chunk_size=config.chunk_size,             # 分割后的文本段最大长度
            chunk_overlap=config.chunk_overlap,       # 连续文本段之间的字符重叠数量
            separators=config.separators,             # 自然段落划分的符号
            length_function=len,                      # 使用python自带的len函数做长度统计的依赖
        )      # 文本分割器的对象

    def upload_by_str(self,data:str,filename):
        """将传入的字符串，进行向量化，存入向量数据库中"""
        # 先得到出传入的字符串的md5值
        md5_hex=get_string_md5(data)
        if check_md5(md5_hex):
            return "[Repeat] 内容已存在知识库"
        if len(data) > config.max_spliter_char_number:
            knowledge_chunks:list[str]=self.spliter.split_text(data) # 类型统一，均用列表套字符串
        else:
            knowledge_chunks=[data]

        metadata={
            "source":filename,
            #2026-3-8 15:43:30
            "create_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator":"客户",
        }

        self.chroma.add_texts(        # 内容加载到向量库中
            # iterable-> list \tuple
            knowledge_chunks,
            metadata=[metadata for _ in knowledge_chunks],

        )
        save_md5(md5_hex)
        return "[Success]内容已经成功载入向量库"

if __name__ =='__main__':
    # r1 = get_string_md5("周杰伦")
    # r2 = get_string_md5("周杰伦")
    # r3 = get_string_md5("周杰伦4")
    # # 为什么用md5  哈希算法（散列函数）能把任意长度数据，算出一串32位16进制的字符串
    # #优点： 快 简单 能做简单文件校验   ，缺点：  不能做安全加密   易于被破解，过时
    # #SHA-256  SHA-512
    #
    # print(r1)
    # print(r2)
    # print(r3)

    #save_md5("7a8941058aaf4df5147042ce104568da")
    #print(check_md5("7a8941058aaf4df5147042ce104568da"))
    service= KnowledgeBaseService()
    r=service.upload_by_str("流星","testfile")
    print(r)