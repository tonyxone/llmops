#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/6/2024 4:26 PM
@Author :Tony
@File   :exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomException(Exception):
    """基础自定义一场信息"""
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    """通用失败异常"""
    pass


class NotFoundException(CustomException):
    """未找到数据异常"""
    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    """未授权异常"""
    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    """无权限异常"""
    code = HttpCode.FORBIDDEN


class ValidateErrorException(CustomException):
    code = HttpCode.VALIDATE_ERROR
