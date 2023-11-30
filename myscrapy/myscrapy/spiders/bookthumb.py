# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MyscrapyItem
from os.path import join
import re

#name不能过长,不能有问号,|号
def getteachernamebookname(bookname):
    if(bookname==None):
        return '[]',''
    bookname=bookname.replace('?','!').replace('|','').replace('/','%').replace('*','').replace('<','').replace('>','').replace(':',';').strip()
    try:
        teacher=re.search('\[.*?\]',bookname).group()
    except Exception as e:
        teacher='[]'
    if (teacher=='[]'):
        name=bookname[:120].strip()
    else:
        try:
            name=re.search('\].*?\[',bookname).group()[1:-1].strip()
        except Exception as e:
            name=bookname.split("]")[-1][:120].strip()
    return teacher,name
class ImgSpider(CrawlSpider):
    name = 'bookthumb'
    allowed_domains = ['thedoujin.com']
    def start_requests(self):
        url = 'http://thedoujin.com/index.php/categories/{}'
        num = getattr(self, 'num', None) 
        if num is not None:  
            urlformatted = url.format(num)
        # nums=['257310']
        # for num in nums:
        #     urlformatted=num
        #     if(not num.startswith('http')):
        #         urlformatted = url.format(num)
            yield scrapy.Request(urlformatted,self.parse)

    
    '''
    def firstimgparse(self, response):
        item = MyscrapyItem()
        bookname = response.css('.breadcrumbs a')[-1].css('a::text').get()
        teacher=re.search('\[.*?\]',bookname).group()
        bookname=re.search('\].*?\[',bookname).group()[1:-1].replace('?','')
        booknum=response.url.split('/')[-1]
        pagenum='1'
        item['imgpath'] = join(teacher,booknum+' '+bookname,pagenum)
        item['image_urls'] = [response.css('#image-container img::attr(src)').get()]
        yield item
    '''
    def parse(self, response):
        bookname=response.css('.breadcrumbs span')[-1].css('span::text').get()
        #名字以[]为判断标准,不能有问号,也不能有空格
        teacher,bookname=getteachernamebookname(bookname)
        booknum=response.url.split('/')[-1]
        #封面
        # firstpageformation='http://thedoujin.com/index.php/pages/{}'
        # firstpageurl=firstpageformation.format(booknum)
        # yield scrapy.Request(firstpageurl,self.firstimgparse)
        firstthumbitem = MyscrapyItem()
        pagenum='1'
        firstthumbitem['imgpath'] = join('bookthumb',teacher,booknum+' '+bookname,pagenum)
        firstthumbitem['image_urls'] = [response.css('.row img::attr(src)').get()]
        yield firstthumbitem
        #所有的cols
        for col in response.css('.col'):
            item = MyscrapyItem()
            pagenum=col.css('a::attr(href)').get().split('=')[-1]
            item['imgpath'] = join('bookthumb',teacher,booknum+' '+bookname,pagenum)
            item['image_urls'] = [col.css('img::attr(data-src)').get()]
            yield item
