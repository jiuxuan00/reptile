from urllib.request import urlretrieve
import requests
import re
import json

# 获取页面
def getPage(url):
    res=requests.get(url)
    if res.status_code==200:
        return res.text


# 解析页面
def parasePage(html):
    pattern=re.compile('<a.*?dimg="(.*?)">(.*?)</a>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'image':'http://www.xunmoban.com' + item[0],
            'name':item[1],
            'type':item[0].split('/')[-1].split('.')[1]
        }
        # print(item)
        # print('http://www.xunmoban.com'+item)


# 下载图片
def downImg(image,type,name):
    html=requests.get(image)
    with open(name + '.' + type,'wb') as file:
        file.write(html.content)


def main():
    url='http://www.xunmoban.com/demo/demopic.php?aid=735'
    html=getPage(url)
    for item in parasePage(html):
        downImg(item['image'], item['type'], item['name'])
        # print(item)


if __name__=='__main__':
    main()