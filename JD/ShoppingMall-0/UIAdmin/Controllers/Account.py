#!/usr/bin/env python
# -*- coding:utf-8 -*-
from ..Core.HttpRequest import AdminRequestHandler


class Login(AdminRequestHandler):

    def get(self, *args, **kwargs):

        self.render('Account/Login.html')

    def post(self, *args, **kwargs):
        pass



class LoginOut(AdminRequestHandler):

    def get(self, *args, **kwargs):

        self.render('Account/Login.html')

