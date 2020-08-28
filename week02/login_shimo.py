#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 10:57
# @Author  : huzunyan
# @File    : login_shimo
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://shimo.im/login?from=home')
time.sleep(1)

username = browser.find_element_by_name('mobileOrEmail')
username.send_keys('15895981485')
time.sleep(1)

password = browser.find_element_by_name('password')
password.send_keys('123456')
time.sleep(1)


submit = browser.find_element_by_xpath('//div/button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]')
submit.click()
time.sleep(5)

cookies = browser.get_cookies()  # 获取cookies
print(cookies)
