# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import re
from os.path import join
from twisted.enterprise import adbapi
import pymysql

class MyscrapyPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的叫做实例方法。
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        #读取settings中配置的数据库参数
        dbparams = dict(
            host=settings['MYSQL_HOST'],  
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        #python 3.x 不再支持MySQLdb，它在py3的替代品是： import pymysql。
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    # pipeline默认调用
    def process_item(self, item, spider):
        # query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        # query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def _conditional_insert(self, tx, item):
        #ignore repalce ON DUPLICATE KEY UPDATE当插入的记录遇到主键或者唯一键重复时，会执行后面定义的UPDATE操作。
        sql = "insert ignore into indexfull(id,md5,description) values(%s,"+'0x'+item['md5']+",%s)"
        params = (item['bookid'],item['description'][:1023])
        tx.execute(sql, params)

    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print(failue)

class MyImagesPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'referer': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52',
    }
    def get_media_requests(self, item, info):
        # request_objs=super(MyImagesPipeline, self).get_media_requests(item,info)
        # for request_obj in request_objs:
        #     request_obj.item=item
        # return request_objs
       for image_url in item['image_urls']:
            self.default_headers['referer'] = image_url
            # 没有对应item直接崩错
            try:
                yield scrapy.Request(image_url,headers=self.default_headers,meta={'cookiejar': item['cookie'],'item':item})
            except Exception as e:
                yield scrapy.Request(image_url,meta={'item':item})

    def file_path(self, request, response=None, info=None):
    #根本不进这个方法
        path=super(MyImagesPipeline, self).file_path(request,response,info)
        # imgpath=request.item.get('imgpath')
        imgpath=request.meta['item'].get('imgpath')
        imgpath=imgpath+path[-4:]
        return imgpath

                
            
        
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        #if not image_paths:
            #raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
        