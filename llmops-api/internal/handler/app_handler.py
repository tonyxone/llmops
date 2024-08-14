#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/3/2024 10:18 AM
@Author :Tony
@File   :app_handler.py
"""
import uuid
from dataclasses import dataclass

from injector import inject
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
	"""应用控制器"""

	app_service: AppService

	def create_app(self):
		"""调用服务创建新的app记录"""
		app = self.app_service.create_app()
		return success_message(f"应用已经成功创建，id为{app.id}")

	def get_app(self, id: uuid.UUID):
		app = self.app_service.get_app(id)
		return success_message(f"应用成功获取，名字是{app.name}")

	def update_app(self, id: uuid.UUID):
		app = self.app_service.update_app(id)
		return success_message(f"应用成功更新，名字是{app.name}")

	def delete_app(self, id: uuid.UUID):
		app = self.app_service.delete_app(id)
		return success_message(f"应用已经成功删除，id为{app.id}")

	def debug(self, app_id: uuid.UUID):
		"""聊天接口"""

		# 1.提取从接口中获取的输入,post
		req = CompletionReq()
		if not req.validate():
			return validate_error_json(req.errors)

		# 2.构建组件
		prompt = ChatPromptTemplate.from_template("{query}")
		llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
		parser = StrOutputParser()

		# 3.构建链
		chain = prompt | llm | parser

		# 4.执行链
		content = chain.invoke({"query": req.query.data})

		return success_json({"content": content})
