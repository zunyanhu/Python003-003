#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 15:50
# @Author  : huzunyan
# @File    : job_02
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com


def double(x):
    return x * 2


def my_map(func, iterable):
    str_tmp = []
    for i in iterable:
        each_one = func(i)
        str_tmp.append(each_one)
    return str_tmp.__iter__()


string = [1, 2, 3, 4, 5]
res = my_map(double, string)
print(list(res))
