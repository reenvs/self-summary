# -*- coding: utf-8 -*-
import scrapy


class HelloSpider(scrapy.Spider):
    name = "hello"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        pass
