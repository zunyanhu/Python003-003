# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem
from scrapy.selector import Selector
import requests
from bs4 import BeautifulSoup as bs


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films']
    cookie = {
        'Cookie': '__mta=188159895.1597930494297.1597933287735.1597936222205.5; uuid_n_v=v1; uuid=ED9C1CF0E2E911EAABD8ED85325F9646A75A97940C984E488F3C57D4CD99758D; mojo-uuid=00fff337c7bbcf5870fc9c4512788d01; _lxsdk_cuid=1740c1458d6c8-0c4a1c383279e9-31657305-13c680-1740c1458d6c8; _lxsdk=ED9C1CF0E2E911EAABD8ED85325F9646A75A97940C984E488F3C57D4CD99758D; _csrf=a55093a14e592a96d21aba38aa37595db4958fa59775fe3b707059419290308a; mojo-session-id={"id":"c090917532b3add4b4459cf061bbbe6b","time":1598084222046}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597930494,1598073057,1598084222; mojo-trace-id=3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598084224; __mta=188159895.1597930494297.1597936222205.1598084224534.6; _lxsdk_s=17415126af2-265-63f-fa9%7C%7C11'}

    def parse(self, response):
        url_list = response.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
        count = 0
        for url in url_list:
            link = 'https://maoyan.com' + url.root
            count += 1
            if count > 10:
                break
            yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        item = MaoyanItem()
        film_name = response.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()').extract()[0]
        film_type = response.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a//text()').extract()
        release_time = response.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').extract()[0]
        print(film_name)
        print(film_type)
        print(release_time)
        item['film_name'] = film_name
        item['film_type'] = ''.join(film_type)
        item['release_time'] = release_time
        yield item