#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Model.Product import IProductRepository
from Model.Product import Product
from Model.Product import Price


class ProductRepository(IProductRepository):

    def __init__(self):
        self.conn = ""

    def fetch_all(self):

        model_obj_list = []

        # 根据参数拼接SQL，执行
        sql = """ select * from tb """

        # 获取数据库结果
        result = [
            {'nid': '1', 'name': 'seven', 'rrp': 10, 'selling_price': 9},
        ]

        # 循环所有的结果，格式化为模型
        for item in result:
            model_obj_list.append(Product(nid=item['nid'],
                                          name=item['name'],
                                          price=Price(rrp=item['rrp'],
                                                      selling_price=item['selling_price']
                                                      )
                                          )
                                  )
        return model_obj_list
