#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyType(type):

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)


        # print(obj)
        print('首先执行')


        obj.__init__(*args, **kwargs)
        # obj.__init__(666)
        return obj

class Foo(metaclass=MyType):
    def __init__(self, name):
        print('第二次执行')
        self.name = name

    def f1(self):
        print(self.name)

obj = Foo(123)
print(obj)
print(obj.name)
