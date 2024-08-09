#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/6/2024 10:09 PM
@Author :Tony
@File   :test_app_handler.py
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    """app控制器的测试类"""

    @pytest.mark.parametrize("query", [None, "你好,你是?"])
    def test_completion(self, query, client):
        r = client.post("/app/completion", json={"query": query})
        assert r.status_code == 200
        if query is None:
            assert r.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert r.json.get("code") == HttpCode.SUCCESS
