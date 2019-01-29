#获取QQ好友头像，保存在image文件夹中

import requests,json,os
import math 
import PIL.Image as Image 


def getImage(qq_num):
	url = 'http://q1.qlogo.cn/g?b=qq&nk='+qq_num+'&s=140&t=961118830'
	print (url)
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}	
	resp = requests.get(url,headers=headers)
	return resp

def writeImage(i):
	with open('./friends/'+i,encoding='utf-8') as f:
		num = f.read()
		zzz = json.loads(num[10:-2])['data']['uinlist']
		for i in zzz:
			print (i)
			responsess = getImage(i['data'])
			with open('./image' + "/" + str(i['data']) + ".jpg",'wb+') as ff:
				ff.write(responsess.content)

def allImage():
	ls = os.listdir('./image')
	each_size = int(math.sqrt(float(640*640)/len(ls))) 
	lines = int(640/each_size) 
	image = Image.new('RGB', (640, 640))
	x = 0 
	y = 0 
	for i in ls: 
		print (i)
		try:
			img = Image.open('./image' + "/" +i) 
		except IOError: 
			print("Error") 
		else: 
			img = img.resize((each_size, each_size), Image.ANTIALIAS) 
			image.paste(img, (x * each_size, y * each_size)) 
			x += 1 
			if x == lines: 
				x = 0 
				y += 1 
	image.save('./image' + "/" + "all.jpg")


dirs = os.listdir('./friends')
for i in dirs:
	writeImage(i)

allImage()
