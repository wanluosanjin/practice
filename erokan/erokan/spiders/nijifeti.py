import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random

class ImgSpider(CrawlSpider):
    name = 'nijifeti'
    ready = 0
    allowed_domains = ['nijifeti.com'] 
    def start_requests(self):
        # num = int(getattr(self, 'num', None))
        num = getattr(self, 'num', None)
        if(num=="1"):
            url="https://nijifeti.com/"
            # cookies=self.cookies
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        else:
            url='https://nijifeti.com/page/{}'
            url=url.format(num)
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        
    def parse(self, response):
        imgpagelist=response.css(".posts article .posts__item-title a::attr(href)").getall()
        firstimgs=response.css(".posts article a::attr(style)").getall()
        for index,firstimg in enumerate(firstimgs):
            item = ErokanItem()
            item["image_urls"] = [firstimg.split("'")[-2]]
            item['cookie'] = response.meta['cookiejar']
            item['net'] = "nijifeti"
            yield item
        if(int(response.url.split('/')[-1])>=200):
            for imgpage in imgpagelist:
                yield scrapy.Request(imgpage,self.imgpageparse200,meta = {'cookiejar': response.meta['cookiejar']})
        else:
            for imgpage in imgpagelist:
                yield scrapy.Request(imgpage,self.imgpageparse,meta = {'cookiejar': response.meta['cookiejar']})
    def imgpageparse(self, response):
        item = ErokanItem()
        # image-urls必须是列表
        item["image_urls"] = response.css(".post__main li a::attr(href)").getall()
        item['cookie'] = response.meta['cookiejar']
        item['net'] = "nijifeti"
        yield item
    def imgpageparse200(self, response):
        item = ErokanItem()
        # image-urls必须是列表
        item["image_urls"] = response.css(".post__content a::attr(href)").getall()
        item['cookie'] = response.meta['cookiejar']
        item['net'] = "nijifeti"
        yield item
