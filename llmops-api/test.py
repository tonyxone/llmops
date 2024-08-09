#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/3/2024 9:59 AM
@Author :Tony
@File   :test.py
"""

from injector import inject, Injector


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A's name:{self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
