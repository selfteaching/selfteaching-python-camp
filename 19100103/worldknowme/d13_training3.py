# -*- coding: utf-8 -*-
# 微信无法登陆网页版，所以用Day11的链接代替
#第一步，处理链接文字
import re
import jieba
from collections import Counter
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')   #获取微信公众号文章返还结果'response'
from pyquery import PyQuery
document=PyQuery(response.text)       #将内容抓取下来
content=document('#js_content').text()      #获取正文内容
import stats_word_d11
s = stats_word_d11.stats_text_cn(content,20)        #引用stats.text 来统计20个词
#s = str(s)                                        #转为字符串str类型
print(s)
# 第二步，统计完毕DAY11 作业中的链接20个词，接下来进行图标处理
################################################################################################################
import matplotlib.pyplot as plt
import numpy as np     

x=[]
y=[]
strResult=''
for temp in s:
        x.append(temp[0])
        y.append(temp[1])
print(x)
print(y)
strResult=','.join([str(a) for a in s])

plt.rcdefaults()
fig, ax = plt.subplots()
y_pos=np.arange(len(x))
ax.barh(y_pos, y, align='center',color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(x)
ax.invert_yaxis()  
ax.set_xlabel('词组名称')
ax.set_title('连接中词组对应的词频数示意图')

from pylab import mpl                          # 设置动态参数解决Matplotlib图标输出中文显示问题，处理方法详见 https://blog.csdn.net/u010758410/article/details/71743225    
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.savefig('picture.png')
plt.show()                        #显示图片
