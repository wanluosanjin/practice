# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MyscrapyItem
from os.path import join
import re

class BookFullSpider(CrawlSpider):
    name = 'bookfull'
    allowed_domains = ['thedoujin.com']
    page = ''
    def start_requests(self):
        self.page = getattr(self, 'num', None) 
        categoriesurl='https://thedoujin.com/index.php/categories/{}'

        if self.page is not None:  
            categoriesurlformatted = categoriesurl.format(self.page)
        yield scrapy.Request(categoriesurlformatted,self.parse,meta = {'cookiejar': 1})

    def parse(self, response):
        categoriestart='https://thedoujin.com/index.php/categories/'
        if(response.url.startswith(categoriestart)):
            page1url='https://thedoujin.com/index.php/pages/{}'
            page2url='https://thedoujin.com/index.php/pages/{}?Pages_page={}'
            urls=[]
            imgnum=len(response.css('.col').getall())+1
            urls.append(page1url.format(self.page))
            for num in range(2,imgnum+1):
                urls.append(page2url.format(self.page,num))
            for url in urls:
                yield scrapy.Request(url,self.fullimgparse,meta={'cookiejar': response.meta['cookiejar']})

    def fullimgparse(self,response):
            item = MyscrapyItem()
            #get()似乎等同于extract_first()
            #extract等于转string
            bookname = response.css('.breadcrumbs a')[-1].css('a::text').get()
            bookurl = response.css('.breadcrumbs a')[-1].css('a::attr(href)').get() 
            teacher='[]'
            bookname=re.sub(r"[\\/:\*\?<>\"\|]","%",bookname)
            #消除非法字符
            teachersearch=re.search(r'(\[.*?\])(.*)',bookname)
            if(teachersearch):
                teacher=teachersearch.group(1)
            booknum=bookurl.split('/')[-1]
            pagenum = response.css('.breadcrumbs span::text').get().split(' ')[-1]
            item['imgpath'] = join('erokan','bookfull',teacher,(booknum+" "+bookname)[:255],pagenum)
            item['image_urls'] = [response.css('#image-container img::attr(src)').get()]
            item['cookie'] = response.meta['cookiejar']
            yield item
    

