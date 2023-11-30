import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random

class ImgSpider(CrawlSpider):
    name = 'bookthumb'
    allowed_domains = ['thedoujin.com']
    def start_requests(self):
        # num = int(getattr(self, 'num', None))
        num = getattr(self, 'num', None)
        url = 'https://thedoujin.com/index.php/categories/{}'
        num = getattr(self, 'num', None) 
        if num is not None:  
            urlformatted = url.format(num)
            yield scrapy.Request(urlformatted,self.parse,meta = {'cookiejar': 1})
        
    def parse(self, response):
        bookname=response.css('.breadcrumbs span')[-1].css('span::text').get()
        teacher='[]'
        bookname=re.sub(r"[\\/:\*\?<>\"\|]","%",bookname)
        #消除非法字符
        teachersearch=re.search('(\[.*?\])(.*)',bookname)
        if(teachersearch):
            teacher=teachersearch.group(1)
        booknum=response.url.split('/')[-1]
        for col in response.css('.col'):
            item = ErokanItem()
            item['net'] = self.name
            pagenum=col.css('a::attr(href)').get().split('=')[-1]
            item['path'] = join(self.name,teacher,booknum,pagenum+".jpg")
            item['image_urls'] = [col.css('img::attr(data-src)').get()]
            item['cookie'] = response.meta['cookiejar']
            yield item