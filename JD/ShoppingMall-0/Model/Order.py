#!/usr/bin/env python
# -*- coding:utf-8 -*-


class IOrderRepository:

    def update(self, entity):
        """
        更新某个实体
        :param entity:
        :return:
        """

    def add(self, entity):
        """
        添加一个实体
        :param entity:
        :return:
        """

    def remove(self, entity):
        """
        删除实体
        :param entity:
        :return:
        """

    def fetch_all(self):
        """
        获取所有
        :return:
        """

    def fetch_one_by_nid(self, nid):
        """
        根据ID获取值
        :param nid: 主键ID
        :return:
        """


class Foo:
    """值对象"""
    def __init__(self):
        self.name = None
        self.email = None


class Order:
    """领域模型"""
    def __init__(self):
        self.nid = None
        self.orderDate = None
        self.customId = None
        self.foo = Foo()


class OrderService:

    def __init__(self, order_repository):
        self.orderRepository = order_repository

    def find_all_customer_orders_by(self, nid):
        """
        业务相关方法
        :param nid: 唯一主键ID
        :return: 领域模型对象
        """

        customer_order_list = self.orderRepository.fetch_one_by_nid(nid)

        return customer_order_list



