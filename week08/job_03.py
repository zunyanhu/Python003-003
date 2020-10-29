#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 10:09
# @Author  : huzunyan
# @File    : job_03
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import time
import random
from functools import wraps


# def timer(func):
#     def call_fun(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(f'程序用时：{end_time-start_time}秒')
#     return call_fun

def timer(func):
    """
    用装饰器实现函数计时器
    """
    @wraps(func)
    def func_timer(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'程序用时：{end_time-start_time}秒')
        return res
    return func_timer




@timer
def sum_start_end(start, end):
    """
    需要被执行计时器的函数
    """
    sum = 0
    for n in range(start, end+1):
        sum += n
        time.sleep(random.uniform(0, 1))
    print(f'计算结果为：{sum}')



if __name__ == "__main__":
    sum_start_end(1, 10)
