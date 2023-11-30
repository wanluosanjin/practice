# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErokanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    pagenum = scrapy.Field()
    cookie = scrapy.Field()
    net = scrapy.Field()
    path = scrapy.Field()
    description = scrapy.Field()
    bookid = scrapy.Field()
