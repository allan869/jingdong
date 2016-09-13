#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .Controllers import Account

patterns = [
    (r"/login.html$", Account.Login),
]