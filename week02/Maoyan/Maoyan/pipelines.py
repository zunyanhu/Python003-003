# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MaoyanPipeline(object):
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'spider_data')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '')
        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')

    def process_item(self, item, spider):
        self.db_cur = self.db_conn.cursor()
        self.insert_db(item)
        return item

    def insert_db(self, item):
        sql = """INSERT INTO maoyanfilm_data(film_name, film_type, release_time) VALUES ('%s', '%s', '%s')""" % (
        item['film_name'], item['film_type'], item['release_time'])
        try:
            self.db_cur.execute(sql)
            self.db_conn.commit()
        except Exception as e:
            print(f'发生异常：{e}')
            self.db_conn.rollback()
        finally:
            self.db_cur.close()

    def close_spider(self, spider):
        self.db_conn.close()
