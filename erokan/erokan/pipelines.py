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
from urllib import parse
import time
import random
class ErokanPipeline(object):
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
        if(spider.name=="indexthumb"):
            query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
            query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def moeimgsql(self, tx, item):
        #ignore repalce ON DUPLICATE KEY UPDATE当插入的记录遇到主键或者唯一键重复时，会执行后面定义的UPDATE操作。
        # params%s会加""不能用来写入MD5
        for index,image in enumerate(item["images"]):
            md5=image['path'].split('\\')[-1].split('.')[0]
            sql = "insert ignore into img values(null,"+"0x"+md5+",%s)"
            # 不能用imgname有的文件可能没下
            description="m "+item['pagenum']+" "+image["url"].split("/")[-1].split(".")[0]
            params = (description)
            tx.execute(sql, params)
    def nijifetisql(self, tx, item):
        for image in item["images"]:
            md5=image['path'].split('\\')[-1].split('.')[0]
            sql = "insert ignore into img values(null,"+"0x"+md5+",%s)"
            description="n2 "+image["url"].split("/")[-1].split(".")[0]
            params = (description)
            tx.execute(sql, params)
    def momonijisql(self, tx, item):
        for image in item["images"]:
            md5=image['path'].split('\\')[-1].split('.')[0]
            sql = "insert ignore into img values(null,"+"0x"+md5+",%s)"
            description="m2 "+image["url"].split("/")[-1].split(".")[0]
            params = (description)
            tx.execute(sql, params)
    def nijixsql(self, tx, item):
        for image in item["images"]:
            md5=image['path'].split('\\')[-1].split('.')[0]
            sql = "insert ignore into img values(null,"+"0x"+md5+",%s)"
            description="n3 "+item["pagenum"]+" "+image["url"].split("-")[-1].split(".")[0]
            params = (description)
            tx.execute(sql, params)
    def nijinchusql(self, tx, item):
        for index,image in enumerate(item["images"]):
            md5=image['path'].split('\\')[-1].split('.')[0]
            sql = "insert ignore into img values(null,"+"0x"+md5+",%s)"
            description="ni "+image["url"].split("/")[-1].split(".")[0]
            params = (description)
            tx.execute(sql, params)
    def _conditional_insert(self, tx, item):
        #ignore repalce ON DUPLICATE KEY UPDATE当插入的记录遇到主键或者唯一键重复时，会执行后面定义的UPDATE操作。
        sql = "insert ignore into indexthumb values(%s,%s)"
        params = (item['bookid'], item['description'][:1023])
        tx.execute(sql, params)

    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print(failue)

class MyImagesPipeline(ImagesPipeline):
    moeimg = {
        'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '',
        'Connection':'keep-alive',
        'Host':'img.moeimg.net',
        'referer': 'http://moeimg.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    }
    nijinchu = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '',
        'Connection':'keep-alive',
        'Host':'nijinchu.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    }
    imgnijinchu = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '',
        'Connection':'keep-alive',
        'Host':'img.nijinchu.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    }
    nijifeti = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '',
        'Connection':'keep-alive',
        'Host':'nijifeti.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    }
    bookfull = {
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
        if(item["net"]=="moeimg"):
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url,headers=self.moeimg,meta={'cookiejar': item['cookie'],'item':item})
        elif(item["net"]=="nijinchu"):
            for image_url in item['image_urls']:
                # 一定要!=-1,-1会被识别为true
                if(image_url.find("img.nijinchu.com")!=-1):
                    yield scrapy.Request(image_url,headers=self.imgnijinchu,meta={'cookiejar': item['cookie'],'item':item})
                if(image_url.find("nijinchu.com")!=-1):
                    yield scrapy.Request(image_url,headers=self.nijinchu,meta={'cookiejar': item['cookie'],'item':item})
        elif(item["net"]=="nijifeti"):
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url,headers=self.nijifeti,meta={'cookiejar': item['cookie'],'item':item})
        elif(item["net"]=="bookfull"):
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url,headers=self.bookfull,meta={'cookiejar': item['cookie'],'item':item})
        else:
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url,meta={'cookiejar': item['cookie'],'item':item})
        # self.default_headers['referer'] = image_url
        # 没有对应item直接崩错
        # try:
        #     yield scrapy.Request(image_url,headers=self.default_headers,meta={'cookiejar': item['cookie'],'item':item})
        # except Exception as e:
        #     yield scrapy.Request(image_url,meta={'item':item})

    # 除了request其他几个根本不能用
    # 除了request其他几个必须等none
    def file_path(self, request, response=None, info=None, *, item=None):
        net=request.meta['item'].get('net')
        if(net=='indexthumb'):
            path=request.meta['item'].get('path')
            # return join(net,teacher.strip()[:255],bookid+" "+bookname.strip()[:255]+path[-4:])
            return path
        if(net=='bookthumb'):
            path=request.meta['item'].get('path')
            return path
        if(net=='bookfull'):
            path=request.meta['item'].get('path')
            return path
        path=super(MyImagesPipeline, self).file_path(request,response,info)
        imgnames=request.url.split("/")
        filename=imgnames[-1].split(".")[0]
        if(net=='erokan'):
            return join(net,imgnames[-3],imgnames[-2],parse.unquote(filename,errors='replace')+path[-4:])
        return join(net,imgnames[-3],imgnames[-2],filename+path[-4:])
            # if(re.search(r"/\d{14}_\w+\.\w{3}",request.url)!=None):
            #     imgname=request.url.split("/")[-1].split(".")[0]
            #     page=imgname[:14]
            #     filename=imgname[15:]
            #     return join(net,page,filename+path[-4:])
            # if(re.search(r"/\d+/\w{11,14}\.\w{3}",request.url)!=None):
            #     filename=request.url.split("/")[-1].split(".")[0]
            #     page=request.url.split("/")[-2]
            #     return join(net,page,filename+path[-4:])
            # if(re.search(r"/\w+-\d+-\d+.*",request.url)!=None):
            #     imgname=request.url.split("/")[-1].split(".")[0]
            #     imgnames=imgname.split("-")
            #     if(len(imgnames)==2):
            #         return join(net,imgnames[0],imgnames[1]+path[-4:])
            #     if(len(imgnames)==3):
            #         return join(net,imgnames[0]+"-"+imgnames[1],imgnames[2]+path[-4:])
            #     if(len(imgnames)==4):
            #         return join(net,imgnames[0]+"-"+imgnames[1],imgnames[2]+"-"+imgnames[3]+path[-4:])
            #     return join(net,imgname+path[-4:])
            # if(re.search(r"\w+\d{9}",request.url)!=None):
            #     imgname=request.url.split("/")[-1].split(".")[0]
            #     if(imgname[-2]!="-"):
            #         page=imgname[:-3]
            #         filename=imgname[-3:]
            #         return join(net,page,filename+path[-4:])
            #     if(imgname[-2]=="-"):
            #         page=imgname[:-5]
            #         filename=imgname[-5:-2]
            #         return join(net,page,filename+path[-4:])
            #     return join(net,imgname+path[-4:])