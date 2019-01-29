# @Author: Fan Xujing
# @Date:   2018-09-21 11:41:00
# @Email:   961118830@qq.com
# @Last Modified time: 2019-01-29 17:09:58
#qq好友分布情况，

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

def chartP(x,y):
	#设置字体
	myfont = font_manager.FontProperties(fname='C:/Windows/Fonts/STXINWEI.TTF')

	plt.figure(figsize=(10,6))

	#画出柱状图
	plt.bar(x,y,width = 0.55,align='center',color = 'r',alpha=0.8)

	#设置x轴的刻度，将构建的xticks代入，同时由于省份类目文字较多，在一块会比较拥挤和重叠，
	#因此设置字体和对齐方式
	#fontproperties 指定字体
	plt.xticks(x,x,size='small',rotation=30,fontproperties=myfont)

	#x、y轴标签与图形标题
	# plt.xlabel('省份',fontproperties=myfont)
	# plt.ylabel('number')
	# plt.title('QQ好友地区分布图',fontproperties=myfont)

	plt.xlabel('年龄',fontproperties=myfont)
	plt.ylabel('数量')
	plt.title('QQ好友年龄分布图',fontproperties=myfont)

	#设置数字标签
	for a,b in zip(x,y):
		plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)

	#设置y轴的范围
	plt.ylim(0,130)
	plt.savefig("persionInfo/zage.jpg")
	plt.show()


if __name__ == '__main__':
	# #设置x轴柱子的个数
	# x=['湖北', 'None', '广东', '新疆', '黑龙江', '山东', '山西', '安徽', '上海', '江苏', '浙江', '河北', '云南', '北京', '重庆', '甘肃', '首尔', '内蒙古', '福建', '河南', '湖南', '维多利亚', '天津'] #课程品类数量已知为14，也可以用len(ppv3.index)

	# #设置y轴的数值，需将numbers列的数据先转化为数列，再转化为矩阵格式
	# y=[146, 106, 9, 1, 2, 1, 2, 2, 11, 4, 6, 6, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	
	chartP(x,y)