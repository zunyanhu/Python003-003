#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 11:06
# @Author  : huzunyan
# @File    : urls
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
]