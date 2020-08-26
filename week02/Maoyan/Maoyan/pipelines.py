# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MaoyanPipeline(object):
    # def process_item(self, item, spider):
    #     film_name = item['film_name']
    #     film_type = item['film_type']
    #     release_time = item['release_time']
    #     data = f'{film_name}|{film_type}|{release_time}\n'
    #     with open('./maoyanfilm.txt', 'a', encoding='utf-8') as article:
    #         article.write(data)
    #     return item
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'spider_data')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '')

        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            item['film_name'],
            item['film_type'],
            item['release_time'],
        )

        sql = 'INSERT INTO maoyanfilm_data VALUES(%s,%s,%s)'
        self.db_cur.execute(sql, values)
