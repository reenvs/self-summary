# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title=scrapy.Field()
	href=scrapy.Field()
	time=scrapy.Field()
	content=scrapy.Field()
