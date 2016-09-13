#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .Response import UserResponse
from .ModelView import UserModelView


class UserService:

    def __init__(self, model_user_service):
        self.modelUserService = model_user_service

    def check_login(self, user_request):
        response = UserResponse()

        try:
            model = self.modelUserService.check_login(user_request.username, user_request.email, user_request.password)
            if not model:
                raise Exception('用户名或密码错误')
            else:
                model_view = UserModelView(nid=model['nid'],
                                           username=model['usename'],
                                           email=model['email'],
                                           last_login=model['last_login'],
                                           user_type_id=model['user_type'].nid,
                                           user_type_caption=model['user_type'].caption,
                                           vip_type_id=model['vip_type'].nid,
                                           vip_type_caption=model['vip_type'].caption,)
                response.modelView = model_view
        except Exception as e:
            response.status = False
            response.message = str(e)


