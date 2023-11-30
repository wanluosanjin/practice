# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
     bookid = scrapy.Field()
     md5 = scrapy.Field()
     description = scrapy.Field()
     image_urls = scrapy.Field()
     imgpath = scrapy.Field()
     image_paths = scrapy.Field()
     cookie=scrapy.Field()