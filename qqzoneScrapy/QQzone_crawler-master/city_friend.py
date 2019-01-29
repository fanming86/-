# city_friend.py
# 调用 province_chart 生成好友省份分布直方图

import province_chart
import os,json

ls = os.listdir('./persionInfo')

# print(ls)

def count_num():
	nn = vv = oo = 0
	province = []
	province_all = []
	for i in ls:
		if 'info' in i:
			with open('persionInfo/'+i,encoding='utf-8') as f:
				file_content = f.read()
			print(i)
			file_co= json.loads(file_content[11:-3].replace('\n', ''))
			if 'error' in file_co:
				print(file_co)
			elif file_co['province'] not in province:
				province.append(file_co['province'])
				province_all.append(file_co['province'])
			else:
				province_all.append(file_co['province'])
		else:
			break
	return province,province_all


li1,li2 = count_num()
labels = []
quants = []
title = 'province'
# print(li1)
for x in li1:
	if not x:
		labels.append('None')
		quants.append(li2.count(x))
	else:
		Num = li2.count(x)
		quants.append(Num)
		labels.append(x)
		print(x,Num)
# print(labels,quants)

province_chart.chartP(labels,quants)
