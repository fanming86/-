# sec_analysis.py
# 生成好友性别比例饼图
#男性为1,
#读取persionInfo 目录下的文件

import secss
import os,json

ls = os.listdir('./persionInfo')

# print(ls)

def count_num():
	nn = vv = oo = 0
	for i in ls:
		if 'info' in i:
			with open('persionInfo/'+i,encoding='utf-8') as f:
				file_content = f.read()
			file_co= json.loads(file_content[11:-3].replace('\n', ''))
			if 'error' in file_co:
				print(file_co)
			else:
				# print(file_co['sex'])
				if file_co['sex'] == 1:
					nn += 1
				elif file_co['sex'] == 2:
					vv += 1
				else:
					oo += 1
		else:
			break
	return ([nn,vv,oo])



labels = ['sir', 'ms', 'Othoer']
quants = count_num()
title = u'Friend gender map'

secss.draw_pie(labels,quants,title)