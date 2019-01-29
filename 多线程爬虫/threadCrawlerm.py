# @Author: Fan Xujing
# @Date:   2018-09-21 11:41:58
# @Email:   961118830@qq.com
# @Last Modified time: 2018-11-17 10:42:05
# 正则表达式、多线程、队列、抓取豆瓣电影top250

import requests
import re
import time
import threading
from queue import Queue


class thread_crawl(threading.Thread):
    '''
    抓取线程类
    '''
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q

    def run(self):
        print ("开始获取原始网页，线程id为： " + self.threadID)
        self.movies_spider()
        print ("退出线程： ", self.threadID)

    def movies_spider(self):
        # page = 1
        while True:
            if self.q.empty():
                break
            else:
                page = self.q.get()
                print ('douban_spider=', self.threadID, ',page=', str(page))
                url = 'https://movie.douban.com/top250?start='+str(page)+'&filter='
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                    'Accept-Language': 'zh-CN,zh;q=0.8'}
                # 多次尝试失败结束、防止死循环
                timeout = 3
                while timeout > 0:
                    timeout -= 1
                    try:
                        content = requests.get(url, headers=headers)
                        data_queue.put(content.text)
                        break
                    except Exception as e:
                        print ('qiushi_spider', e)
                if timeout < 0:
                    print ('timeout', url)



class Thread_Parser(threading.Thread):
    '''
    页面解析类；
    '''
    def __init__(self, threadID, data_queue, lock, f):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.queue = data_queue
        self.lock = lock
        self.f = f

    def run(self):
        print ('Thread_Parser starting ', self.threadID)
        global total, exitFlag_Parser
        while not exitFlag_Parser:       	
            try:
                '''
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且block为False，队列将引发Empty异常。
                '''
                item = self.queue.get(False)
                # print (item)
                self.parse_data(item)
                self.queue.task_done()
                print ('Thread_Parser=', self.threadID, ',total=', total)
            except Exception as e:
                pass
        print ('Thread_Parser Exiting ', self.threadID)

    def parse_data(self, item):
        '''
        解析网页函数
        :param item: 网页内容
        :return:
        '''
        global total
        try:
            ree = re.compile(u'<div.*?class="item">.*?'
                            +u'<div.*?class="pic">.*?'
                            +u'<em.*?class="">(.*?)</em>.*?'			#排行名次
                            +u'<div.*?class="info">.*?'
                            +u'<div.*?class="hd">.*?'
                            +u'<a.*?href=".*?".*?class="">.*?'
                            +u'<span class="title">(.*?)</span>.*?'				#电影名称
                            +u'<span class="other">&nbsp;/&nbsp;(.*?)</span>.*?</a>.*?'		#别名
                            +u'<div.*?class="bd">.*?<p.*?class="">.*?'
                            +u'导演:(.*?)&nbsp;&nbsp;&nbsp;.*?<br>'
                            +u'(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;'		#上映时间、制片国家
                            +u'(.*?)</p>.*?<div.*?class="star">.*?'		#电影类型
                            +u'<span.*?'
                            +u'class="rating_num".*?property="v:average">'
                            +u'(.*?)</span>.*?'							#电影评分
                            +u'.*?<span>(.*?)人评价</span>.*?'		#评价人数
                            +u'<p.*?class="quote">.*?'
                            +u'<span.*?class="inq">(.*?)'		#短评
                            +u'</span>.*?</p>',re.S|re.I)
            content = ree.findall(item)
            print(content)
            if content:
                for i in content:
                    self.f.write('排名：'+i[0]+'\n')
                    self.f.write('电影名称：'+i[1]+'\n')
                    self.f.write('别名：'+i[2].lstrip('&nbsp;/&nbsp;')+'\n')
                    self.f.write('导演：'+i[3].lstrip('&nbsp;/&nbsp;')+'\n')
                    self.f.write('年份：'+i[4].strip()+'\n')
                    self.f.write('国家：'+i[5].strip()+'\n')
                    self.f.write('类型：'+i[6].strip()+'\n')
                    self.f.write('评分：'+i[7].strip()+'\n')
                    self.f.write('参评人数：'+i[8].strip()+'\n')
                    self.f.write('短评：'+i[9].strip()+'\n')
                    self.f.write('\n')
            else:
            	print('content is Null')
        except Exception as e:
            print ('parse_data: ', e)
        with self.lock:
            total += 1


data_queue = Queue()	#用来存放原始数据的队列
exitFlag_Parser = False
lock = threading.Lock()
total = 0

def main():
	pageQueue = Queue(50)	#用来存放页码数的队列
	for page in range(0,226,25):
	    pageQueue.put(page)

	#初始化采集线程
	crawlthreads = []
	crawlList = ["crawl-1", "crawl-2", "crawl-3"]

	for threadID in crawlList:
	    thread = thread_crawl(threadID, pageQueue)
	    thread.start()
	    crawlthreads.append(thread)


	#初始化解析线程parserList
	parserthreads = []
	parserList = ["parser-1", "parser-2", "parser-3"]
	f = open('movies.txt','w+',encoding='utf-8')
	#分别启动parserList
	for threadID in parserList:
	    thread = Thread_Parser(threadID, data_queue, lock, f)
	    thread.start()
	    parserthreads.append(thread)

	# 等待队列清空
	while not pageQueue.empty():
		pass
	# 等待所有线程完成
	for t in crawlthreads:
	    t.join()
	print('thread_crawl线程结束')

	while not data_queue.empty():
	    pass

	# 通知线程是时候退出
	global exitFlag_Parser
	exitFlag_Parser = True

	for t in parserthreads:
	    t.join()

	print ("Exiting Main Thread")
	with lock:
	    f.close()


if __name__ == '__main__':
    main()