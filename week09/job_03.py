#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 10:09
# @Author  : huzunyan
# @File    : job_03
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import time
import random


def timer(func):
    def call_fun(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'程序用时：{end_time-start_time}秒')
    return call_fun


@timer
def sum_start_end(start, end):
    sum = 0
    for n in range(start, end+1):
        sum += n
        time.sleep(random.uniform(0, 1))
    print(f'计算结果为：{sum}')


sum_start_end(1, 10)
