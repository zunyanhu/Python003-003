#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 14:26
# @Author  : huzunyan
# @File    : urls
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'film_review'
urlpatterns = [
    path('', views.film_review),
    url('search/', views.search, name='search'),
]