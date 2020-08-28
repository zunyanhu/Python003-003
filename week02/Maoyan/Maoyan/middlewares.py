# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from . import my_proxies


class MaoyanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MaoyanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomProxyMiddleware(object):

    def process_request(self, request, spider):
        ip = random.choice(my_proxies.proxy_list)
        print('测试IP:', ip)
        request.meta['proxy'] = f'http://{ip}'


class CheckProxyMiddleware(object):
    def process_response(self, request, response, spider):
        print('代理IP:', request.meta['proxy'])
        return response


from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, ConnectionRefusedError, ConnectionDone, ConnectError, ConnectionLost, TCPTimedOutError
from scrapy.http import HtmlResponse
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError


class ExceptionMiddleware(object):
    ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError)

    def process_response(self, request, response, spider):
        if str(response.status).startswith('4') or str(response.status).startswith('5'):
            response = HtmlResponse(url='')
            return response
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.ALL_EXCEPTIONS):
            print('Got exception: %s' % (exception))
            response = HtmlResponse(url='exception')
            return response
        print('not contained exception: %s' % exception)


import requests
import time


class ProxyMiddleware(object):

    def __init__(self):
        self.s = requests.session()

    def process_request(self, request, spider):
        time.sleep(5)
        try:
            proxy_url = spider.settings.get('PROXY_URL')
            r = self.s.get(proxy_url)
            proxy_ip_port = r.text.replace('\n', '').replace('\r', '')
            request.meta['proxy'] = 'http://' + proxy_ip_port
        except requests.exceptions.RequestException:
            print('***get proxy fail!')

    def process_response(self, request, response, spider):
        if response.status != 200:
            try:
                proxy_url = spider.settings.get('PROXY_URL')

                r = self.s.get(proxy_url)
                proxy_ip_port = r.text.replace('\n', '').replace('\r', '')
                request.meta['proxy'] = 'http://' + proxy_ip_port
            except requests.exceptions.RequestException:
                print('***get proxy fail!')

            return request
        return response

    def process_exception(self, request, exception, spider):

        try:
            proxy_url = spider.settings.get('PROXY_URL')

            r = self.s.get(proxy_url)
            proxy_ip_port = r.text.replace('\n', '').replace('\r', '')
            request.meta['proxy'] = 'http://' + proxy_ip_port
        except requests.exceptions.RequestException:
            print('***get proxy fail!')

        return request
