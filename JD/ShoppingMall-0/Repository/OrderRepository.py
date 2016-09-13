#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Model.Order import IOrderRepository


class OrderRepository(IOrderRepository):

    def __init__(self):
        self.conn = ""

    def update(self, entity):
        pass

    def add(self, entity):
        pass

    def remove(self, entity):
        pass

    def fetch_all(self):
        pass

    def fetch_one_by_nid(self, nid):
        pass
