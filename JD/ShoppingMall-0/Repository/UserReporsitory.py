#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Model.User import IUseRepository
from Model.User import User
from Model.User import UserType
from Model.User import VipType
from .DbConnection import DbConnection


class ProductRepository(IUseRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_one_by_email_pwd(self, email, password):
        ret = None

        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from UserInfo where email=%s and password=%s"""
        cursor.execute(sql, (email, password))
        db_result = cursor.fetchone()
        self.db_conn.close()
        print(type(db_result), db_result)
        if db_result:
            ret = User(nid=db_result['nid'],
                       username=db_result['username'],
                       email=db_result['email'],
                       last_login=db_result['last_login'],
                       user_type=UserType(nid=db_result['user_type']),
                       vip_type=VipType(nid=db_result['vip'])
                       )
        return ret

    def fetch_one_by_user_pwd(self, username, password):
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from UserInfo where username=%s and password=%s"""
        cursor.execute(sql, (username, password))
        db_result = cursor.fetchone()
        self.db_conn.close()

        if db_result:
            ret = User(nid=db_result['nid'],
                       username=db_result['username'],
                       email=db_result['email'],
                       last_login=db_result['last_login'],
                       user_type=UserType(nid=db_result['user_type']),
                       vip_type=VipType(nid=db_result['vip'])
                       )
        return ret

    def update_last_login_by_nid(self, nid, current_date):
        cursor = self.db_conn.connect()
        sql = """update UserInfo set last_login=%s where nid=%s"""
        cursor.execute(sql, (current_date, nid))
        self.db_conn.close()