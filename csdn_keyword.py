import requests
from lxml import etree
import pandas
import pandas as pd
import os
import csv
from bs4 import BeautifulSoup


headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }

def parse(url,title,li):
    keyword=li
    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    texts = ' '.join(html.xpath('//div[@id="content_views"]//text()'))
    if len(texts) > 0:
        with open(f'./{li}/{title}.txt', 'w', encoding='utf8') as f:
            f.write(texts)


def spider(url,page,li):
  
        file_name = './' + li
        if not os.path.exists(file_name):
            os.mkdir(file_name)
        params={
            'q':li,
            't':'all',
            'p':page,
            'platform':'pc',
            }

        r = requests.get(url=url, headers=headers, params=params).json()
        #print(r)
        for i in r['result_vos']:
                  url = i['url']
                  title = i['title'].replace('<em>', '').replace('</em>', '').replace('/', '').replace(':', '').replace('*','').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '').replace('.', '')
                  parse(url, title,li)
                  print(title)


if __name__ == '__main__':
    url = "https://so.csdn.net/api/v2/search?"
    lis=['信息安全']
    for li in lis:
        for page in range(1, 21):
            spider(url, page,li)
            print("第", page, "页完成!")