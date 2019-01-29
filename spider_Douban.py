# @Author: Fan Xujing
# @Date:   2018-09-21 11:40:59
# @Email:   961118830@qq.com
# @Last Modified time: 2018-11-17 10:29:12

from urllib import request 
import re
import pymysql

class MovieTop:
	def __init__(self):
		self.param = '&filter='
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
		self.movie_list=[]
		self.file_path = 'movies.txt'

	def get_page(self,start):
		try:
			url = 'https://movie.douban.com/top250?start='+str(start)
			req = request.Request(url,headers = self.headers)
			response = request.urlopen(req)
			page = response.read().decode('utf-8')
			page_num = (start/25+1)
			print('正在抓取第'+str(page_num)+'页数据...')
			# self.start+=25 
			return page 
		except request.URLError as e:
			if hasattr(e,'reason'):
				print('抓取失败，失败的原因是：',e.reason)

	def get_movie_info(self,page):
		pattern = re.compile(u'<div.*?class="item">.*?'
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
		# while self.start<25:
		# page = self.get_page(start)
		movies = re.findall(pattern,page)
		for movie in movies:
			self.movie_list.append([movie[0],movie[1],
				movie[2].lstrip('&nbsp;/&nbsp;'),
				movie[3].lstrip('&nbsp;/&nbsp;'),
				movie[4].lstrip(),
				movie[5].lstrip(),
				movie[6].rstrip(),
				movie[7].lstrip(),
				movie[8],
				movie[9],
				])

	def write_text(self):
		print('开始向文件写入数据......')
		file_top = open(self.file_path,'a',encoding='utf-8')
		try:
			for movie in self.movie_list:
				file_top.write('电影排名：'+movie[0]+'\r\n')
				file_top.write('电影名称：'+movie[1]+'\r\n')
				file_top.write('电影别名：'+movie[2]+'\r\n')
				file_top.write('导演姓名：'+movie[3]+'\r\n')
				file_top.write('上映年份：'+movie[4]+'\r\n')
				file_top.write('制作国家：'+movie[5]+'\r\n')
				file_top.write('电影类别：'+movie[6]+'\r\n')
				file_top.write('电影评分：'+movie[7]+'\r\n')
				file_top.write('参评人数：'+movie[8]+'\r\n')
				file_top.write('简短影评：'+movie[9]+'\r\n\r\n')
			print('抓取结果写入文件成功...')
		except Exception as e:
			print(e)
		finally:
			file_top.close()

	# def main(self):
	# 	for i in range(0,100,25):
	# 		print('开始从豆瓣获取数据......',i)
	# 		self.get_movie_info(i)
	# 		self.write_text()
	# 		print('数据抓取完毕......')


if __name__ == '__main__':
	douban_spider = MovieTop()
	for i in range(0,100,25):
		page = douban_spider.get_page(i)	#i 为页数
		douban_spider.get_movie_info(page)	#将数据存入列表
		douban_spider.write_text()			#将列表中的数据写入文件