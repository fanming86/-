import requests
import lxml
from lxml import etree
import threading
import requests
import re
import time
threadLock = threading.Lock()
def getPage(page,f):
	threadLock.acquire()
# url = 'http://rrl360.com/chanpin/zhaopian?source=5b483d3714fbd&page='
	url = 'http://www.runoob.com/python/python-exercise-example'+str(page)+'.html'
	# 字典
	header = {}
	# 用户代理
	header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	header['Accept-Language'] = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
	header['Content-Type'] = 'text/css'
	header['Accpt'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	header['Accept-Encoding']= 'gzip, deflate'

	res = requests.get(url,headers=header)
	res.encoding=('utf8')
	# print(res.encoding)
	hht = etree.HTML(res.text)

	result = hht.xpath(r'//div[@class="article-intro"]/p/text()')

	print(result)
	for i in result:
		# print(i)
		f.write(i+'\n')
	f.write('\n')
		# pass
	threadLock.release()
def main():
	start_time = time.ctime()
	print('开始从豆瓣获取数据……%s' % start_time)
	with open('douban1.txt','w+',encoding='utf-8') as f:
		for x in range(0,101):
			getPage(x,f)
	stop_time = time.ctime()
	print('获取数据完成！%s' % stop_time)
if __name__=='__main__':
	main()