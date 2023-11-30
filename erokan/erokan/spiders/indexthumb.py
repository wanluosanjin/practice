import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random

class ImgSpider(CrawlSpider):
    name = 'indexthumb'
    allowed_domains = ['thedoujin.com'] 
    def start_requests(self):
        # num = int(getattr(self, 'num', None))
        num = getattr(self, 'num', None)
        if(num=="1"):
            url="https://thedoujin.com/index.php/categories/index"
            # cookies=self.cookies
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        else:
            url='https://thedoujin.com/index.php/categories/index?Categories_page={}'
            url=url.format(num)
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})
        
    def parse(self, response):
        for col in response.css('.col'):
            item = ErokanItem()
            bookid = col.css('a::attr(href)').get().split('/')[-1]
            description=col.css('img::attr(alt)').get()
            item['description'] = description
            item['bookid'] = bookid
            item['image_urls'] = [col.css('img::attr(data-src)').get()]
            item['cookie'] = response.meta['cookiejar']
            # net必须保留
            item['net'] = self.name
            descriptionlastindex=description.find(" - ")
            descriptionlast=description[descriptionlastindex+3:]
            teacher='[]'
            bookname=re.sub(r"[\\/:\*\?<>\"\|]","%",descriptionlast)
            #消除非法字符
            teachersearch=re.search('(\[.*?\])(.*)',bookname)
            if(teachersearch):
                teacher=teachersearch.group(1)
                # bookname=teachersearch.group(2)
            item['path'] = join(self.name,teacher.strip()[:255],bookid+".jpg")
            yield item