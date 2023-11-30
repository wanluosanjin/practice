# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MyscrapyItem
from os.path import join
import re

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
    name = 'indexthumb'
    allowed_domains = ['thedoujin.com']
    #start_urls = ['http://thedoujin.com/index.php/categories/index?tags=tankoubon']
    url='http://thedoujin.com/index.php/categories/index?Categories_page={}'
    start_urls =['http://thedoujin.com/index.php/categories/index']
    for a in range(8000,8870):#8868 #8000完了
        start_urls.append(url.format(a))
    

    def parse(self, response):
        for col in response.css('.col'):
            item = MyscrapyItem()
            #get()似乎等同于extract_first()
            #extract等于转string
            bookname = col.css('.doujinTitle::text').get()
            bookurl = col.css('a::attr(href)').get()
            # bookurl = response.urljoin(bookurl)
            #item['image_urls'] = [col.css('img::attr(data-src)').get()]
            teacher,bookname=getteachernamebookname(bookname)
            item['description']=col.css('img::attr(alt)').get()
            item['bookurl']=bookurl
            #if(not os.path.exists(join('C:\img',teacher))):
            #    os.mkdir(join('C:\img',teacher))
            item['imgpath']=join('indexthumb',teacher,bookurl.split("/")[-1]+' '+bookname)
            yield item
            #必须输出.jpg,前面不能卡否则掠过
            
    ''' print(response)
        #for page_url in response.css('li.next-page a::attr(href)').extract():
            #page_url = response.urljoin(page_url)
            # 将解析出的href里的链接自动判断补全
            #yield scrapy.Request(url=page_url, callback=self.parse)
        for article in response.css('tr.torrent-info trusted'):
            name = article.css('td.tr-name home-td a::text')
            magnet = article.css('td.tr-links home-td a::attr(href)')
            yield {
                    'title' : name.extract_first(),
                    'html' : magnet.extract_first(),
                     }'''

