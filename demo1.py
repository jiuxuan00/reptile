import requests
import re
import json
from requests.exceptions import RequestException
from multiprocessing import Pool



# 1.获取页面内容
def getPageContent(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None


# 2.解析页面
def parsePage(html):
    pattern = re.compile('<li.*?media' +
                         '.*?pic.*?data-src="(.*?)".*?alt="(.*?)".*?</div>' +
                         '.*?sActor.*?<a.*?>(.*?)</a>' +
                         '.*?</li>', re.S)
    items=re.findall(pattern, html)
    for item in items:
        yield {
            'image': item[0],
            'name': item[1],
            'actor': item[2].strip('&nbsp;')
        }


# 3.写入文件
def writeFile(content):
    with open('result2.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

#
def main(offset):
    url='http://tv.2345.com/-neidi----'+str(offset)+'.html'
    html=getPageContent(url)

    for item in parsePage(html):
        print(item)
        writeFile(item)







if __name__=='__main__':
    # main()
    pool=Pool()
    pool.map(main, [i for i in range(20)])