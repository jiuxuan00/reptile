import requests
import re
import json
from requests.exceptions import RequestException   #处理错误
from multiprocessing import Pool



# 获取页面
def getPage(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None


# 解析页面
def parasePage(html):
    pattern=re.compile('<div.*?card-item.*?<img.*?src="(.*?)".*?alt="(.*?)".*?</a>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'image':item[0].replace('http://www.seebd.cc/wp-content/themes/Git-alpha/timthumb.php?src=',''),
            'name':item[1]
        }


# 写入文件
def writePage(content):
    with open('seedb.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()



def main(offset):
    url='http://www.seebd.cc/remen/page/'+str(offset)
    html=getPage(url)
    for item in parasePage(html):
        print(item)
        writePage(item)

if __name__=='__main__':
    # main()
    pool=Pool()
    pool.map(main, [i for i in range(5)])