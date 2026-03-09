import os
import json
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict
from typing import Sequence


def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")

class FileChatMessageHistory(BaseChatMessageHistory):

    def __init__(self,session_id,storage_path):
        self.session_id=session_id
        self.storage_path=storage_path
        # 完整的文件路径
        self.file_path =os.path.join(self.storage_path,self.session_id)
        # 确保文件夹存在
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)
    def add_messages(self, messages: Sequence[BaseMessage])->None:
        # Sequence序列 类似list \ tuple
        all_messages=list(self.messages) # 已有的消息列表
        all_messages.extend(messages)    # 新的和已有的融合成一个list
        #
        # new_messages=[]
        # for message in all_messages:
        #     d=message_to_dirt(message)
        #     new_messages.append(d)d
        new_messages=[message_to_dict(message) for message in all_messages]
        # 将数据写入文件
        with open(self.file_path,"w",encoding="utf-8")as f:
            json.dump(new_messages,f)
    @property     #装饰器将message方法编程成员属性用
    def messages(self)-> list[BaseMessage]:
        # 当前文件内： list[字典]
        try:
            with open(self.file_path,"r",encoding="utf-8")as f:
                message_data= json.load(f)    # 返回值就是：list 字典
                return messages_from_dict(message_data)
        except (FileNotFoundError,json.JSONDecodeError):        # 只捕获filenotfound，但未处理JSONDecodeError等其他异常

            """当以历史纪录文件存在但内容为空，或损坏时，例如手动清空文件或写入不完整，JSON.load(F)会抛出JSONDecoderERROR，导致系统崩溃"""

            return []

    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8")as f:
                json.dump([],f)


