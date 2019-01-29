# city_friend.py
# 调用 province_chart 生成好友省份分布直方图

import province_chart
import os,json

ls = os.listdir('./persionInfo')

# print(ls)

def count_num():
	nn = vv = oo = 0
	age = []
	province_all = []
	gt40 = 0	#大于40岁的好友
	lt18 = 0 	#小于18岁的好友
	for i in ls:
		if 'info' in i:
			with open('persionInfo/'+i,encoding='utf-8') as f:
				file_content = f.read()
			print(i)
			file_co= json.loads(file_content[11:-3].replace('\n', ''))
			if 'error' in file_co:
				print(file_co)
			elif file_co['age'] not in age:
				if int(file_co['age']) > 40:
					gt40 +=1 
				elif int(file_co['age']) <= 18:
					lt18 +=1
				else:
					age.append(file_co['age'])
					province_all.append(file_co['age'])
			else:
				province_all.append(file_co['age'])
		else:
			break
	return age,province_all,lt18,gt40


li1,li2,lt18,gt40 = count_num()
# print(li1,li2)
labels = []
quants = []
labels.append('<18(含)')
quants.append(lt18)
for x in li1:
	if not x:
		labels.append('None')
		quants.append(li2.count(x))
	else:
		Num = li2.count(x)
		quants.append(Num)
		labels.append(str(x))
		print(x,Num)
labels.append('>40(含)')
quants.append(gt40)

print(labels,quants)

province_chart.chartP(labels,quants)
