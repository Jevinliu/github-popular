# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PopularItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    language = scrapy.Field()
    star = scrapy.Field()
    network = scrapy.Field()
    todayStar = scrapy.Field()
    pass
