#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :9/8/2024 10:02 PM
@Author :Tony
@File   :1.对话消息历史组件基础.py
"""

from langchain_community.chat_message_histories import PostgresChatMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()

chat_history.add_user_message("你好，我是慕小课，你是谁?")
chat_history.add_ai_message("你好，我是ChatGPT,有什么可以帮到您?")

print(chat_history)

PostgresChatMessageHistory
