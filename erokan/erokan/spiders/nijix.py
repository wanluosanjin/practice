import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random

class ImgSpider(CrawlSpider):
    name = 'nijix'
    ready = 0
    allowed_domains = ['nijix.net'] 
    def start_requests(self):
        # num = int(getattr(self, 'num', None))
        num = getattr(self, 'num', None)
        if(num=="1"):
            url="https://nijix.net/"
            # cookies=self.cookies
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        else:
            url='https://nijix.net/page/{}/'
            url=url.format(num)
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        
    def parse(self, response):
        imgpagelist=response.css("main #list a::attr(href)").getall()
        for imgpage in imgpagelist:
            yield scrapy.Request(imgpage,self.imgpageparse,meta = {'cookiejar': response.meta['cookiejar']})
    def imgpageparse(self, response):
        item = ErokanItem()
        # image-urls必须是列表
        imgs = response.css("main article a::attr(href)").getall()
        item["image_urls"] =[]
        for img in imgs:
            if(img.find(".wp.com/nijix.net/wp-content")!=-1):
                item["image_urls"].append(img)
        item["pagenum"] = response.url.split("-")[-1].split("/")[0]
        item['cookie'] = response.meta['cookiejar']
        item['net'] = "nijix"
        yield item
