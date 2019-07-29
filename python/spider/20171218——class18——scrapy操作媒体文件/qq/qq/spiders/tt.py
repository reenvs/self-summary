# -*- coding: utf-8 -*-
import scrapy


class TtSpider(scrapy.Spider):
    name = "tt"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        pass
