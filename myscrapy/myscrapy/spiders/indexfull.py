import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MyscrapyItem
from os.path import join
import re

class IndexFullSpider(CrawlSpider):
    name = 'indexfull'
    allowed_domains = ['thedoujin.com']
    def start_requests(self):
        num = int(getattr(self, 'num', None))
        urllist=[]
        categoriesurl='http://thedoujin.com/index.php/categories/index?Categories_page={}'
        for n in range(num,num+10):
            urllist.append(categoriesurl.format(n))
        for url in urllist:
            yield scrapy.Request(url,self.parse,meta = {'cookiejar': 1})

    def parse(self, response):
        for col in response.css('.col'):
            item = MyscrapyItem()
            #这网站img的src属性写在datasrc里
            imgurl = col.css('img::attr(data-src)').get()
            bookid = col.css('a::attr(href)').get().split('/')[-1]
            md5=imgurl[-36:-4]
            description=col.css('img::attr(alt)').get()
            fullimg='https://www.thedoujin.com/images/{}/{}/{}'
            item['image_urls'] = [fullimg.format(imgurl[-36:-34],imgurl[-34:-32],imgurl[-36:])]
            item['bookid'] = bookid
            item['md5'] = md5
            item['description'] = description
            item['imgpath'] = join('indexfull',md5)
            item['cookie'] = response.meta['cookiejar']
            yield item