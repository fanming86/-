#生成饼图

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
 
def draw_pie(labels,quants,title):
    # make a square figure
    plt.figure(1, figsize=(6,6))
    # For China, make the piece explode a bit
    # expl = [0,0,0.05]   #第二块即China离开圆心0.1
    # Colors used. Recycle if not enough.
    colors  = ["blue","red","coral","green","yellow","orange"]  #设置颜色（循环显示）
    # Pie Plot
    # autopct: format of "percent" string;百分数格式
    #explode=expl,
    plt.pie(quants,  colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)
    plt.title(title)   #标题
    plt.savefig("persionInfo/pie.jpg")
    plt.show()
    plt.close()
 
# quants: GDP
 
# labels: country name

if __name__ == '__main__':
    labels   = ['sir', 'ms', 'Othoer']
    quants   = [15094025.0, 11299967.0, 4457784.0, ]
    title = u'test pie'
    draw_pie(labels,quants,title)