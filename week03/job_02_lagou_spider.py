#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:23 上午
# @Author  : huzunyan
# @File    : job_02_lagou_spider.py
# @Software: PyCharm
# @Contact : zunyan.hu@gmail.com
from selenium import webdriver
from multiprocessing import Process
import requests
import time
from lxml import etree


def get_lagou_beijing(url, browser):
    browser.get(url)
    job_search = browser.find_element_by_id('search_input')
    job_search.send_keys('python工程师')
    time.sleep(1)
    submit = browser.find_element_by_id('search_button')
    submit.click()
    time.sleep(3)
    c = browser.get_cookies()
    cookies = {}
    for cookie in c:
        cookies[cookie['name']] = cookie['value']
    headers = {
        'authority': 'www.lagou.com',
        'method': 'GET',
        'path': '/jobs/list_python%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=py',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    print(cookies)
    response = requests.get(url=browser.current_url, cookies=cookies, headers=headers)
    page_text = response.text
    selector = etree.HTML(page_text)
    li_list = selector.xpath('//ul[@class="item_con_list"]/li')
    print(li_list)
    browser.close()


def get_lagou_shanghai():
    pass


def get_lagou_guangzhou():
    pass


def get_lagou_shenzhen():
    pass


def main():
    browser = webdriver.Chrome()
    url_beijing = 'https://www.lagou.com/beijing/'
    p1 = Process(target=get_lagou_beijing, args=(url_beijing, browser))
    p2 = Process(target=get_lagou_guangzhou, )
    p3 = Process(target=get_lagou_guangzhou, )
    p4 = Process(target=get_lagou_shenzhen, )
    p1.start()
    p1.join()


if __name__ == "__main__":
    main()
