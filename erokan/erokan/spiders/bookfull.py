# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErokanItem
from os.path import join
import re
import time
import random

class BookFullSpider(CrawlSpider):
    name = 'bookfull'
    allowed_domains = ['thedoujin.com']
    page = ''
    # 我是傻逼
    bookfull = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie':'',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'none',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    }
    def start_requests(self):
        self.page = getattr(self, 'num', None) 
        categoriesurl='https://thedoujin.com/index.php/categories/{}'

        if self.page is not None:  
            categoriesurlformatted = categoriesurl.format(self.page)
            yield scrapy.Request(categoriesurlformatted,self.parse,meta = {'cookiejar': 1})

    def parse(self, response):
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
        item = ErokanItem()
        #get()似乎等同于extract_first()
        #extract等于转string
        bookname = response.css('.breadcrumbs a')[-1].css('a::text').get()
        bookurl = response.css('.breadcrumbs a')[-1].css('a::attr(href)').get() 
        teacher='[]'
        bookname=re.sub(r"[\\/:\*\?<>\"\|]","%",bookname)
        #消除非法字符
        teachersearch=re.search('(\[.*?\])(.*)',bookname)
        if(teachersearch):
            teacher=teachersearch.group(1)
        booknum=bookurl.split('/')[-1]
        pagenum = response.css('.breadcrumbs span::text').get().split(' ')[-1]
        item['path'] = join('bookfull',teacher,booknum+' '+bookname,pagenum+".jpg")
        item['image_urls'] = [response.css('#image-container img::attr(src)').get()]
        item['cookie'] = response.meta['cookiejar']
        item['net'] = self.name
        yield item