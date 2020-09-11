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

pre_df_1 = pd.read_csv(file_1, encoding='utf-8', sep='\t')
pre_df_1 = pre_df_1.reset_index()
pre_df_1.insert(0, 'id', range(len(pre_df_1)))
pre_df_1.insert(6, 'age', [np.random.randint(0, 100) for _ in range(len(pre_df_1))])
pre_df_1.insert(7, 'order_id', [np.random.randint(1, 1000) for _ in range(len(pre_df_1))])
df_1 = pre_df_1

pre_df_2 = pd.read_csv(file_2, encoding='utf-8', sep='\t')
pre_df_2 = pre_df_2.reset_index()
pre_df_2.insert(0, 'id', range(len(pre_df_2)))
pre_df_2.insert(6, 'age', [np.random.randint(0, 100) for _ in range(len(pre_df_2))])
df_2 = pre_df_2

# SELECT * FROM data;
df1 = df_1
print(f'question 1：\n{df1}\n')

# SELECT * FROM data LIMIT 10;
df2 = df_1.head(10)
print(f'question 2：\n{df2}\n')

# SELECT id FROM data;  //id 是 data 表的特定一列
df3 = df_1['id']
print(f'question 3：\n{df3}\n')

# SELECT COUNT(id) FROM data;
df4 = df3.count()
print(f'question 4：\n{df4}\n')

# SELECT * FROM data WHERE id<1000 AND age>30;
df5 = df_1[(df_1['age'] > 30) & (df_1['id'] < 1000)]
print(f'question 5：\n{df5}\n')

# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df6 = df_1.groupby('id').aggregate({'order_id': 'count'})
print(f'question 5：\n{df6}\n')

# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
df7 = pd.merge(df_1, df_2, on='id')
print(f'question 7：\n{df7}\n')

# SELECT * FROM table1 UNION SELECT * FROM table2;
frames = [df_1, df_2]
df8 = pd.concat(frames)
print(f'question 8：\n{df8}\n')

# DELETE FROM table1 WHERE id=10;
df9 = df_2.drop(df_2[df_2.id == 10].id)
print(f'question 9: \n{df9}\n')

# ALTER TABLE table1 DROP COLUMN column_name;
df10 = df_1.drop(columns='meaning')
print(f'question 10: \n{df10}\n')


