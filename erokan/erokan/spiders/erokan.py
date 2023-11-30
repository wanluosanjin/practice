import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re

class ImgSpider(CrawlSpider):
    name = 'erokan'
    allowed_domains = ['erokan.net'] 
    start_urls =['https://erokan.net']
    def start_requests(self):
        num = getattr(self, 'num', None)
        if(num=="1"):
            url="https://erokan.net/"
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        else:
            url='https://erokan.net/page/{}/'
            url=url.format(num)
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
    def parse(self, response):
        imgpagelist=response.css("#main #list .entry-thumb a::attr(href)").getall()
        for imgpage in imgpagelist:
            yield scrapy.Request(imgpage,self.imgpageparse,meta = {'cookiejar': 1})
    def imgpageparse(self, response):
        item = ErokanItem()
        # image-urls必须是列表
        # 分割后面的缩放参数
        
        image_urls = response.css(".article #the-content img::attr(src)").getall()
        item["image_urls"]=[x.split("?")[0] for x in image_urls]
        # item["title"] = response.css(".article h1::text").get().strip()
        item['net'] = "erokan"
        item['cookie'] = response.meta['cookiejar']
        yield item
