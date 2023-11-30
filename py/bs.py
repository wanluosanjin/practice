#!python3
#利用beauifulsoup筛选给定网页图片url,利用header伪装成浏览器
from bs4 import BeautifulSoup
import requests,random

url = "https://www.mzitu.com/176425/2"
count_time=2

UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

headers = {'User-Agent': random.choice(UserAgent_List)}

'''
#获取页面img
def getimgurl():
    html = requests.get(url, headers=headers)
    #指定网站的编码，查询得到妹子图的编码是gb2312
    html.encoding = 'UTF-8'
    text = html.text #网页html
    #网页html转化为BeautifulSoup对象
    bsop = BeautifulSoup(text, 'html.parser') #parser 构造器
    #找到该页面内的所有图片标签，是一个列表，由上图
    #首先是找class等于postContent的div标签，然后在其中找p标签
    #最后在p标签中找到所有的img标签
    img_list = bsop.find('div', {'id': 'page-current'}).find('a').find('p').findAll('img')
    for img in img_list:
        img_url = img.attrs['src'] #单个图片的真实地址 
        print (img_url)

#下载方法
def download_urls(pages):
    url_imgss = []
    for i in range(1, pages+1):
        try:
            url_list = 'http://www.meizitu.com/a/list_1_' + str(i) + '.html'
            url_imgs = scrawl_list(url_list)
            if not url_imgs:
                continue
            url_imgss.append(url_imgs)
            print("第"+str(i)+"页url_list爬取成功")
            time.sleep(5)
        except:
            continue
    return url_imgss
'''
def scrawl_url(url, proxy_flag=False, try_time=0):
    '''
    此函数的作用是爬取单个图册里面的所有图片的url，一个图册包含几张图片，每个图片有个真实的url地址，需要获取得到
    此函数接收图册url作为参数，如'http://www.meizitu.com/a/5499.html',返回该图册里面所有图片的url列表和图册的名字
    所有图片共用一个名字，可作为文件夹名字存储
    :param url:
    :param proxy_flag:
    :param try_time:
    :return:
    '''
    if not proxy_flag:  # 不使用代理
        try:
            html = requests.get(url, headers=headers,  timeout=10)
            html.encoding = 'UTF-8'
            text = html.text

            bsop = BeautifulSoup(text, 'html.parser')
            img_list = bsop.find('div', {'class': 'main-image'}).find('p').findAll('img')
            print(img_list)
            img_title = bsop.find('div', {'class': 'content'}).find('h2').text

            return img_list, img_title

        except:
            return scrawl_url(url, proxy_flag=True)  # 否则调用自己，使用3次IP代理
        
    else:   # 使用代理时
        if try_time<count_time:
            try:
                print('尝试第'+str(try_time+1)+'次使用代理下载')

                html = requests.get(url, headers=headers, proxies={'http': get_random_ip()},timeout=30)
                html.encoding = 'UTF-8'

                text = html.text
                bsop = BeautifulSoup(text, 'html.parser')
                img_list = bsop.find('div', {'class': 'main-image'}).find('p').findAll('img')
                img_title = bsop.find('div', {'class': 'currentpath'}).find('h2').text

                print('状态码为'+str(html.status_code))
                if html.status_code==200:
                    print('图片通过IP代理处理成功！')
                    return img_list, img_title  # 代理成功下载！
                else:
                    return scrawl_url(url, proxy_flag=True, try_time=(try_time + 1))
            except:
                print('IP代理下载失败')
                return scrawl_url(url, proxy_flag=True, try_time=(try_time+1))  # 否则调用自己，使用3次IP代理
        else:
            print('图片url列表未能爬取，请检查网页')
            return None

def download_img(img_list, img_title):
    '''
    通过scrawl_url函数获得了单个图册里面所有图片的url列表和图册的名字，就可以下载图片了
    此函数的作用下载单个图册里面的所有图片
    接收参数img_list是单个图册里面所有图片的的url，
    如['http://mm.howkuai.com/wp-content/uploads/2017a/02/07/01.jpg',
    'http://mm.howkuai.com/wp-content/uploads/2017a/02/07/02.jpg',...]
    img_title是单个图册的名字，如’香车美女，最完美的黄金搭档‘
    :param img_list:
    :param img_title:
    :return:
    '''

    img_title = format_name(img_title) # 如果图册名字有特殊字符需要处理。不然在windows下保存不了文件夹
    for img_urls in img_list:
        img_url = img_urls.attrs['src'] # 单个图片的url地址
        print(img_url)
        img_html = requests.get(img_url,headers=headers)
        with open(img_title+".jpg", 'wb') as f:
            f.write(img_html.content)
            f.close()

def format_name(img_title):
    '''
    对名字进行处理，如果包含下属字符，则直接剔除该字符
    :param img_title:
    :return:
    '''
    for i in ['\\','/',':','*','?','"','<','>','!','|']:
        while i in img_title:
            img_title = img_title.strip().replace(i, '')
    return img_title

img_list, img_title=scrawl_url(url)
download_img(img_list, img_title)
