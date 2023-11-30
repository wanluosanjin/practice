import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random

class ImgSpider(CrawlSpider):
    name = 'moeimg'
    ready = 0
    allowed_domains = ['moeimg.net'] 
    default_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '',
        'Connection':'keep-alive',
        'Host':'moeimg.net',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    }
    cookies = {
        "_ga":"GA1.2.920506678.1605600733", 
        "__cfduid":"d5af4e7974b06790fa9a629da9b30f8101605600733", 
        "_gid":"GA1.2.1360647443.1606122026"
    }
    def start_requests(self):
        # num = int(getattr(self, 'num', None))
        num = getattr(self, 'num', None)
        if(num=="1"):
            url="http://moeimg.net/"
            # cookies=self.cookies
            yield scrapy.Request(url,self.parse,headers=self.default_headers,meta = {'cookiejar': 1})
        else:
            url='http://moeimg.net/page/{}'
            url=url.format(num)
            yield scrapy.Request(url,self.parse,headers=self.default_headers,meta = {'cookiejar': 1})
        
    def parse(self, response):
        imgpagelist=response.css("#main-2 .post .title a::attr(href)").getall()
        firstimgs=response.css("#main-2 .post .thumb-outer img::attr(src)").getall()
        # posts=response.css(".post") 不要tag了
        # tags=[]
        # for post in posts:
        #     tags.append(post.css(".tag a::text").getall())
        for index,firstimg in enumerate(firstimgs):
            item = ErokanItem()
            item["image_urls"] = [firstimg]
            item["pagenum"] = firstimg.split("/")[-2]
            item['cookie'] = response.meta['cookiejar']
            item['net'] = "moeimg"
            yield item
        for imgpage in imgpagelist:
            yield scrapy.Request(imgpage,self.imgpageparse,headers=self.default_headers,meta = {'cookiejar': response.meta['cookiejar']})
    def imgpageparse(self, response):
        item = ErokanItem()
        # image-urls必须是列表
        item["image_urls"] = response.css(".post .box img::attr(src)").getall()
        item["pagenum"] = response.url.split("/")[-1].split(".")[0]
        item['cookie'] = response.meta['cookiejar']
        item['net'] = "moeimg"
        yield item
