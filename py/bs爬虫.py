#! python3
from bs4 import BeautifulSoup
import requests
import re
import time
url = "https://sukebei.nyaa.net/search/{}?c=_&q=%28%E5%90%8C%E4%BA%BACG%E9%9B%86%29"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
   'Accept': '*/*',
   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
   'Host': 'sukebei.nyaa.net'
    }
'''
def grepurl(url):
    # 2.根据需求构建好链接提取的正则表达式
    pattern1 = '<.*?(href=".*?").*?'
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    #3.模拟成浏览器并爬取对应的网页 谷歌浏览器
    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    page_source = response.read().decode('utf8')
    # 4.根据2中规则提取出该网页中包含的链接
    href1 = re.findall(pattern1,data,re.I)
    href=[]
    for i in href1:
        j=re.search(pattern,i)
        if not j==None:
            href.append(j.group())
    # print(content_href)# 5.过滤掉重复的链接#    # 列表转集合(去重)
    set1 = set(href)
    #写入
    with open('url.txt','w') as f:
        for i in set1:
            f.write(i)
            f.write("\n")
    f.close()
    print('已经生成文件')
    #返回
    return set1
'''
def write(text):
    with open('text2.txt','a',encoding='utf-8') as f:
        f.write(text)#write方法写入后会自动添加换行
        
def gethtml(url):
    session = requests.Session()
    response = session.get(url,headers=headers,allow_redirects=False)
    page_source = response.content.decode()
    #write(page_source)
    return page_source
#
def bsurl(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    text=html.text
    print(text)
    bsop = BeautifulSoup(text, 'html.parser')
    url_list = bsop.find('div', {'id': 'messagelogin'})
    print(url_list)

with open('(同人CG集)3.txt','a',encoding='utf-8') as f:
    for i in range(300,358):
        print(i)
    #gethtml(url)
        bsop = BeautifulSoup(gethtml(url.format(i)))
        for body in bsop.find_all('tbody',class_='alt-colors'):
            for entry in body.find_all('tr'):
                C=entry['class']
                f.write(' '.join(C)+'\n')
                name=entry.find('td',class_='tr-name home-td').a.get_text()
                f.write(name.strip()+'\n')
                magnet=entry.find('td',class_='tr-links home-td').a['href']
                f.write(magnet.strip()+'\n')
                size=entry.find('td',class_='tr-size home-td hide-xs').string
                f.write(size.strip()+'\n')
                S=entry.find('td',class_='tr-se home-td hide-smol').string
                f.write(S+' S\n')
                L=entry.find('td',class_='tr-le home-td hide-smol').string
                f.write(L+' L\n')
                D=entry.find('td',class_='tr-dl home-td hide-xs').string
                f.write(D+' Download\n')
                date=entry.find('td',class_='tr-date home-td date-short hide-xs').string
                f.write(date+'\n')
                f.write('\n')
