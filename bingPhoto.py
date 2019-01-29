# @Author: Fan Xujing
# @Date:   2018-10-13 13:38:09
# @Email:   961118830@qq.com
# @Last Modified time: 2018-10-13 20:07:48

from lxml import etree

import json
import requests
import codecs
import re


headers = {}
headers["User-Agent"]='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
headers["Content-Type"]="application/json;charset=UTF-8"

url = 'https://bing.ioliu.cn/' 
res = requests.get(url,headers=headers)
res.encoding=('utf8')
# print(res.encoding)
hht = etree.HTML(res.text)
result = hht.xpath(r'//div[@class="card progressive"]/a/@href')
imgs = hht.xpath(r'//div[@class="card progressive"]/img/@src')


print(imgs)
for i in result:
	NewUrl = 'https://bing.ioliu.cn'+i 		#大图片所在的页面
	print(NewUrl)


