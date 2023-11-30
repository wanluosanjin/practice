import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random
import requests

class ImgSpider(CrawlSpider):
    name = 'nijinchu'
    allowed_domains = ['nijinchu.com'] 
    def start_requests(self):
        num = getattr(self, 'num', None)
        if(num=="1"):
            url="http://nijinchu.com/"
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        else:
            url='http://nijinchu.com/page/{}/'
            url=url.format(num)
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        
    def parse(self, response):
        imgpagelist=response.css(".entry_list_area .entry_list_element article .entry_list_thumbnail a::attr(href)").getall()
        for imgpage in imgpagelist:
            yield scrapy.Request(imgpage,self.imgpageparse,meta = {'cookiejar': response.meta['cookiejar']})
    def imgpageparse(self, response):
        # image-urls必须是列表
        # item = ErokanItem()
        # imgurls = response.css("#main article p a::attr(href)").getall()
        # item["image_urls"] = []
        # for imgurl in imgurls:
        #     if(imgurl.find("nijinchu.com/img/fullsize/")):
        #         item["image_urls"].append(imgurl)
        # item['cookie'] = response.meta['cookiejar']
        # item['net'] = "nijinchu"
        # if(requests.get(item["image_urls"][0]).status_code!=404):
        #     yield item
        # else:
        item2 = ErokanItem()
        imgurls = response.css("#main article p img::attr(data-lazy-src)").getall()
        item2["image_urls"] = []
        for imgurl in imgurls:
            if(imgurl.find("nijinchu.com/img")):
                item2["image_urls"].append(imgurl)
        item2['cookie'] = response.meta['cookiejar']
        item2['net'] = "nijinchu"
        yield item2