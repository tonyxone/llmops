#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :8/7/2024 10:42 PM
@Author :Tony
@File   :module.py
"""
from flask_migrate import Migrate
from injector import Binder, Module

from internal.externsion.database_extension import db
from internal.externsion.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
