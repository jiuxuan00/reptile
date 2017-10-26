import requests
import re
import json
from requests.exceptions import RequestException
from multiprocessing import Pool  #多线程


def getOnePage(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None


def parseOnePage(html):
    # pattern = re.compile('<li.*?media.*?data-src="(.*?)".*?alt="(.*?)".*?>.*?</li>', re.S)
    pattern = re.compile('<li.*?media'+
                            '.*?pic.*?data-src="(.*?)".*?alt="(.*?)".*?</div>'+
                            '.*?sActor.*?<a.*?>(.*?)</a>'+
                         '.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'image':item[0],
            'name':item[1],
            'actor':item[2].strip('&nbsp;'),
        }

def writeToFile(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()



def main(offset):
    url='http://tv.2345.com/-neidi----'+str(offset)+'.html'
    html=getOnePage(url)
    # print(parseOnePage(html))
    for item in parseOnePage(html):
        print(item)
        writeToFile(item)


if __name__=='__main__':
    # main()
    pool=Pool()
    pool.map(main,[i for i in range(100)])
