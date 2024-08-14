#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/13/2024 3:10 PM
@Author :Tony
@File   :2.LCEL表达式简化版.py
"""

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

# 2.创建链
chain = prompt | llm | parser

# 3.执行链
print(chain.invoke({"query": "请讲一个关于程序员的冷笑话"}))
