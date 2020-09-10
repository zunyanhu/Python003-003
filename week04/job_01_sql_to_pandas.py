#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 17:36
# @Author  : huzunyan
# @File    : job_01_sql_to_pandas
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import pandas as pd
import numpy as np
import random

file_1 = 'info_1.csv'
file_2 = 'info_2.csv'


df = pd.read_csv(file_1, encoding='utf-8', sep='\t')
df = df.reset_index()
df.insert(0, 'id', range(len(df)))
# df.insert(4, 'age', random.randint(1, 100))
df.insert(6, 'age', [random.randint(1, 100) for _ in range(len(df))])
pre_df = df

df1 = df
print(f'第一题：\n{df1}\n==============分割线==============')

df2 = df.head(10)
print(f'第二题：\n{df2}\n==============分割线==============')

df3 = df['id']
print(f'第三题：\n{df3}\n==============分割线==============')

df4 = df3.count()
print(f'第四题：\n{df4}\n==============分割线==============')

df5 = df[(df['age'] > 30) & (df['id'] < 1000)]
print(f'第五题：\n{df5}\n==============分割线==============')