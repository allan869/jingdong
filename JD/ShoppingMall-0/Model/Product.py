#!/usr/bin/env python
# -*- coding:utf-8 -*-


class IDiscountStrategy:

    def apply_extra_discounts_to(self, original_sale_price):
        """
        申请格外的折扣
        :param original_sale_price: 原价
        :return:
        """


class NullDiscountStrategy(IDiscountStrategy):

    def apply_extra_discounts_to(self, original_sale_price):
        return original_sale_price


class TradeDiscountStrategy(IDiscountStrategy):

    def apply_extra_discounts_to(self, original_sale_price):

        discounted_price = original_sale_price * 0.9

        return discounted_price


class DiscountFactory:

    @staticmethod
    def get_discount_strategy_for(customer_type):

        if customer_type == CustomerType.Trade:
            return TradeDiscountStrategy()
        else:
            return NullDiscountStrategy()


class CustomerType:

    Standard = 0
    Trade = 1


class Price:

    def __init__(self, rrp, selling_price):
        """
        价格对象
        :param rrp: 原价
        :param selling_price: 售价
        :return:
        """
        self.rrp = rrp
        self.__sellingPrice = selling_price
        self._discountStrategy = NullDiscountStrategy()

    def set_discount_strategy_to(self, discount_strategy):
        self._discountStrategy = discount_strategy

    def get_selling_price(self):

        return self._discountStrategy.apply_extra_discounts_to(self.__sellingPrice)

    sellingPrice = property(fget=get_selling_price)


class Product:

    def __init__(self, nid, name, price):
        self.nid = nid
        self.name = name
        self.price = price


class IProductRepository:

    def fetch_all(self):
        """
        获取所有商品
        :return: 商品列表，即：[模型对象, ]
        """


class ProductService:

    def __init__(self, product_repository):
        self.productRepository = product_repository

    def get_all_product_list_for(self, customer_type):
        """
        获取所有商品列表
        :param customer_type:
        :return: Product对象列表
        """
        product_list = self.productRepository.fetch_all()

        discount_strategy = DiscountFactory.get_discount_strategy_for(customer_type)

        for p in product_list:
            p.price.set_discount_strategy_to(discount_strategy)

        return product_list