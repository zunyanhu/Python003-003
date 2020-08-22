# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        release_time = item['release_time']
        data = f'{film_name}|{film_type}|{release_time}\n'
        with open('./dmaoyanfilm.txt', 'a+', encoding='utf-8') as article:
            article.write(data)
        return item
