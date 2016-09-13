#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import abc
#
# # python实现接口类型方法(用来做约束的)
#
# class IOrderRepository:
#     def fetch_one_by(self, nid):
#         """
#         获取单条数据的方法,所有继承当前类的类必须实现该(有)方法
#         """
#         raise Exception('子类中必须实现该方法')
#
# class OrderRepository(IOrderRepository):
#     def fetch_one_by(self, nid):
#         print(nid)
#
# obj = OrderRepository()
# obj.fetch_one_by(1)
#
# # 抽象方法抽象类(即可以继承,又可以做约束)
#
#
#
# class Foo(metaclass=abc.ABCMeta):
#     def f1(self):
#         print('111')
#
#     def f2(self):
#         print('222')
#
#     @abc.abstractmethod
#     def f3(self):
#         """
#         用来做约束的
#         :return:
#         """
#
#
# class Bar(Foo):
#     def f3(self):
#         print('333')
#
# obj = Bar()
# # 普通继承调用f1,f2方法没有问题,调用f3就会报错,因为f3有约束,只有重写字方法才可以
# obj.f1()
# obj.f2()
# obj.f3()
#
# # 组合
#
# class MyType(type):
#
#     def __call__(cls, *args, **kwargs):
#         obj = cls.__new__(cls, *args, **kwargs)
#
#
#         print('首先执行')
#         obj.__init__(*args, **kwargs)
#         # obj.__init__(666)
#         return obj
#
# class Foo(metaclass=MyType):
#     def __init__(self, name):
#         print('第二次执行')
#         self.name = name
#
#     def f1(self):
#         print(self.name)
#
# obj = Foo(123)
# print(obj)
# print(obj.name)

# 解释器解释
# 1.遇到class Foo,执行type的__init__方法
# 2.Type的init的方法里面做什么,不知道
# obj = Foo(123)
# print(obj)
# print(obj.name)
# 3.执行Type的__call__方法
#     执行Foo类的__new__方法
#     执行Foo类的__init__方法

# 依赖注入

class Mapper:
    __mapper_relation = {}

    @staticmethod
    def register(cls, value):
        Mapper.__mapper_relation[cls] = value

    @staticmethod
    def exit(cls):
        if cls in Mapper.__mapper_relation:
            return True
        return False

    @staticmethod
    def value(cls):
        return Mapper.__mapper_relation[cls]

class MyType(type):

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        arg_list = list(args)
        if Mapper.exit(cls):
            value = Mapper.value(cls)
            arg_list.append(value)

        # print('首先执行')
        obj.__init__(arg_list, **kwargs)
        # obj.__init__(666)
        return obj

class Foo(metaclass=MyType):
    def __init__(self, name):
        print('第二次执行')
        self.name = name

    def f1(self):
        print(self.name)

class Bar(metaclass=MyType):
    def __init__(self, name):
        # print('第二次执行')
        self.name = name

    def f1(self):
        print(self.name)

Mapper.register(Foo, '666')
Mapper.register(Bar, '999')

# obj = Foo(123)
# print(obj)
# print(obj.name)

f = Foo()
print(f.name)
b = Bar()
print(b.name)