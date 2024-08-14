#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/13/2024 2:04 PM
@Author :Tony
@File   :1.手写chain.py
"""
from typing import Any

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()


# 2.构建输入
class Chain:
	steps: list = []

	def __init__(self, steps: list):
		self.steps = steps

	def invoke(self, input: Any) -> Any:
		for step in self.steps:
			input = step.invoke(input)
			print("步骤", step)
			print("输出", input)
			print("==============")
		return input


# 3. 编排链
chain = Chain([prompt, llm, parser])

# 4. 执行链并获取结果
print(chain.invoke({"query": "你好，你是"}))
