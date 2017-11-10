from urllib.request import urlretrieve
import requests
import re
import json
from multiprocessing import Pool


# 获取页面
def getPage(url):
    res=requests.get(url)
    if res.status_code==200:
        return res.text

# 解析页面
def parasePage(html):
    pattern=re.compile('<a.*?href="(.*?)".*?</a>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        print(item)


# 解析内容页
def parasePage2(html):
    # pattern=re.compile('<h1.*?(.*?)</h1>',re.S)
    # items=re.findall(pattern,html)
    print(html)
    # for item in items:
    #     print(item)






def main():
    # url='http://www.shuge.net/html/98/98971/'
    url='http://www.shuge.net/html/4/4694/3291827.html'
    html=getPage(url)
    # for item in parasePage(html):
    parasePage2(html)
    #     # print(item)


if __name__=='__main__':
    main()
    # pool = Pool()
    # pool.map(main, [i for i in range(1)])


