#-*- coding: UTF-8 -*-
import re
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8') #解决写入文件编码不一致问题

if __name__ == "__main__":
    #以CSDN为例，CSDN不更改User Agent是无法访问的
    #url = 'http://www.csdn.net/'
    url = 'https://www.qiushibaike.com/'
    head = {}
    #写入User Agent信息
    #head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    head["User-Agent"] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    req = urllib2.Request(url, headers=head) #创建Request对象
    response = urllib2.urlopen(req)#传入创建好的Request对象
    html = response.read().decode('utf-8')#读取响应信息并解码
   
    #print(html)  #打印信息
    pattern = re.compile('<div.*?class="content.*?>.*?<span>(.*?)</span>',re.S)	  #只匹配段子
    #pattern = re.compile('<span>(.*?)</span>',re.S)
    items = re.findall(pattern,html)
    #print items
    pageStories = []


    s = open('/home/ming/txt/qiubai.txt','w')
   
    for item in items:
	print '***************************************'
        print item
	s.write("    "+item)
	s.write('\n' * 2)
    s.close()

