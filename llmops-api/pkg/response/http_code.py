#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/5/2024 10:57 PM
@Author :Tony
@File   :http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    """HTTP基础业务状态码"""
    SUCCESS = "success"  # 成功状态
    FAIL = "fail"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    VALIDATE_ERROR = "validate_error"
