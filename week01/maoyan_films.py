#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 16:29
# @Author  : huzunyan
# @File    : maoyan_films
# @Software: PyCharm
# @Contact ： zunyan.hu@gmail.com
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def get_film_urls(index_url, headers):
    response = requests.get(index_url, headers=headers)
    bs_info = bs(response.text, 'html.parser')
    film_list = []
    count = 0
    for divs in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}):
        film_url = "https://maoyan.com" + (divs.find('a').get('href'))
        film_list.append(film_url)
        count += 1
        if count == 10:
            break
    return film_list


def get_film_detail(detail_url, headers):
    response = requests.get(detail_url, headers=headers)
    bs_info = bs(response.text, 'html.parser')
    film_name = bs_info.find('h1').text
    for li in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
        film_type = []
        for atag in li.find_all('a', attrs={'class': 'text-link'}):
            film_type.append(atag.string)
        film_type = ''.join(film_type)
        release_time = ''.join(li.find_all(text=re.compile('-')))
        return film_name + '/' + film_type + '/' + release_time


def main():
    index_url = 'https://maoyan.com/films'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Cookie': '__mta=188159895.1597930494297.1597930769590.1597933287735.4; uuid_n_v=v1; uuid=ED9C1CF0E2E911EAABD8ED85325F9646A75A97940C984E488F3C57D4CD99758D; _csrf=8ecef8ba102f3bb57368c64bc678fffdf16894ea92ce5d413996ed3ec6843e71; mojo-uuid=00fff337c7bbcf5870fc9c4512788d01; _lxsdk_cuid=1740c1458d6c8-0c4a1c383279e9-31657305-13c680-1740c1458d6c8; _lxsdk=ED9C1CF0E2E911EAABD8ED85325F9646A75A97940C984E488F3C57D4CD99758D; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597930494; mojo-session-id={"id":"71aba1e49aedf7407f0fb74fade689a7","time":1597933286644}; mojo-trace-id=3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597935055; __mta=188159895.1597930494297.1597933287735.1597935055012.5; _lxsdk_s=1740c3ef4e5-1df-7f6-1e0%7C%7C5'
    }
    film_url_list = get_film_urls(index_url, headers)
    data_list = []
    for detail_url in film_url_list:
        data_list.append(get_film_detail(detail_url, headers))
    movie = pd.DataFrame(data=data_list)
    movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)


if __name__ == "__main__":
    main()
