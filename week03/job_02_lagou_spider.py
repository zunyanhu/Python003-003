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
import lxml


def get_lagou_beijing(url, browser):
    browser.get(url)
    job_search = browser.find_element_by_id('search_input')
    job_search.send_keys('python工程师')
    time.sleep(1)
    submit = browser.find_element_by_id('search_button')
    submit.click()
    time.sleep(3)
    cookies = browser.get_cookies()
    browser.close()
    headers = {
        'Cookie': cookies
    }
    response = requests.get(browser.current_url, headers=headers)
    page_text = response.text
    # money_list = response.xpath('//span[@class="money"]//span/text()').extract()
    # bs_info = bs(response.text, 'html.parser')
    # money_list = bs_info.find_all('span', attrs={'class': 'money'})
    page_text.xpath()
    print(money_list)



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
