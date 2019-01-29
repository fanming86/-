#coding:utf-8


import json
import requests
import sys
import re



headers = {}
headers["User-Agent"]='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
headers["Content-Type"]="application/json;charset=UTF-8"


for i in range(1,9):
    page = str(i)
    url = 'https://www.qiushibaike.com/text/page/%s/' % page
    resp = requests.get(url,headers=headers)
    # result = json.dumps(resp.json(),ensure_ascii=False)

    
    content = resp.text


    pattern = re.compile('<div.*?content">.*?<span>(.*?)</span>.*?</div>.*?<.*?"number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)

    # print items



    for item in items:
        print (item[0])

        with open ('qiubai.txt','ea',encoding='utf-8') as f:
            f.write(item[0])



