# @Author: Fan XuJing
# @Date:   2018-09-13 16:30:14
# @Email:  969756850@qq.com
# @Last Modified time:  2018-09-17 14:57:54

import re,requests
from queue import Queue
import threading



ajax_url='https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=101&sort=0&page=5'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
ajaxResult = requests.get(ajax_url,headers=header)

ajaxDict = ajaxResult.json()['content']
print('已经获取json数据')



#创建线程，photoUrl为图片的地址
class myThread (threading.Thread):
    def __init__(self, threadID,pageQueue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        # self.PhotoUrl = PhotoUrl
        self.pageQueue = pageQueue
    def run(self):
        while True:
            if self.pageQueue.empty():
                break
            else:
                print ("开始线程：%s" % self.threadID)
                timeout = 4
                while timeout > 0:
                    timeout -= 1
                    try:
                        url = self.pageQueue.get()	#从队列中取出图片地址
                        photoResult = requests.get(url,headers=header)
                        data_queue.put(photoResult.content)		#将获取的图片放到新的队列
                        break
                    except Exception as e:
                        print ('获取图片错误：', e)
                    
                if timeout < 0:
                    print ('timeout', url)
                print ("退出线程：%s" % self.threadID)


#开始调用线程
threadLi = []	#用来存放线程

#此队列用来存放图片
data_queue = Queue()

#此队列用来保存图片的地址
pageQueue = Queue()
for i in ajaxDict:
    pageQueue.put(i['image'])
    # print(pageQueue.qsize())	#打印队列的长度


for i in range(10):		#开始启动线程，每次起十个
    threadd = myThread(i,pageQueue)
    threadd.start()
    threadLi.append(threadd)

# 等待队列清空
while not pageQueue.empty():
    pass	

for i in threadLi:
	i.join()       #同步阻塞



i = 0
while True:
	if not data_queue.empty():
		photo = data_queue.get()
		print('开始写入图片%s' % i)
		with open('photo/'+str(i)+'.jpg','ab') as f:
			f.write(photo)
		i += 1
	else:
		break




# resp = requests.get(url,headers=header)

# # print(resp)

# with open('fnegniao.jpg','ab') as f:
# 	f.write(resp.contentd)