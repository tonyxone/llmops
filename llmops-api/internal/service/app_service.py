#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/8/2024 9:52 PM
@Author :Tony
@File   :app_service.py
"""
import uuid
from dataclasses import dataclass

from injector import inject

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.auto_commit():
            # 1.创建模型实体类
            app = App(name="测试机器人", account_id=uuid.uuid4(), icon="", description="")
            # 2.将实体类添加到session会话中
            self.db.session.add(app)
            # 3.提交session会话
        return app

    def get_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return app

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.db.session.query(App).get(id)
            app.name = "bot"
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app
