#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/8/2024 10:32 PM
@Author :Tony
@File   :sqlalchemy.py
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    """重写flask-sqlalchemy中的核心类， 实现自动提交"""

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
