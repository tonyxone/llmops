#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/3/2024 10:32 AM
@Author :Tony
@File   :http.py
"""
import os

from flask import Flask
from flask_migrate import Migrate

from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import Response, json, HttpCode
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):
    """Http服务引擎"""

    def __init__(self,
                 *args,
                 conf: Config,
                 db: SQLAlchemy,
                 router: Router,
                 migrate: Migrate,
                 **kwargs):
        super().__init__(*args, **kwargs)

        # 1.初始化应用配置
        self.config.from_object(conf)

        # 2.注册绑定异常处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 3.初始化数据库
        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")

        # 4.注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))

        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
