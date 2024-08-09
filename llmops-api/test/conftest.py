#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/6/2024 10:14 PM
@Author :Tony
@File   :conftest.py
"""

import pytest

from app.http.app import app


@pytest.fixture
def client():
    """获取Flask应用测试应用，并返回"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
