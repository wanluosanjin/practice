import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random

class ImgSpider(CrawlSpider):
    name = 'momoniji'
    ready = 0
    allowed_domains = ['momoniji.com'] 
    def start_requests(self):
        # num = int(getattr(self, 'num', None))
        num = getattr(self, 'num', None)
        if(num=="1"):
            url="http://momoniji.com/"
            # cookies=self.cookies
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        else:
            url='http://momoniji.com/page/{}/'
            url=url.format(num)
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        
    def parse(self, response):
        uncheckimgpagelist=response.css("#content #main #list a::attr(href)").getall()
        imgpagelist=filter(lambda x: x.find("momoniji.com")!=-1,uncheckimgpagelist)
        # b = [i for i in a if i >5]
        for imgpage in imgpagelist:
            yield scrapy.Request(imgpage,self.imgpageparse,meta = {'cookiejar': response.meta['cookiejar']})
    def imgpageparse(self, response):
        item = ErokanItem()
        # image-urls必须是列表
        item["image_urls"] =filter(lambda x: x.find("momoniji.com")!=-1,response.css("#main article ol li a::attr(href)").getall())
        item['cookie'] = response.meta['cookiejar']
        item['net'] = "momoniji"
        yield item
