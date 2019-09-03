import stats_word
import json
import requests
from pyquery import PyQuery
import yagmail
import getpass
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties 

#获取网页内容
response= requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA', auth=('user', 'pass'))
document = PyQuery(response.text)
content = document('#js_content').text()#获取文本
count=10  #限制输出元素的变量
try: 
    text_list= stats_word.stats_text(content,count) #调用统计汉字的函数
    text_list2=[]#存储词
    text_list3=[]#存储词频
    for i in text_list: 
        text_list2.append(i[0])#把text_list里的词取出来
        text_list3.append(i[1])#把text_list里的数字取出来   
except ValueError as identifier: 
    print('请输入字符串',identifier) 
del text_list2[-2:]#统计的结果后面总是有英文Twitter号之类，删掉
del text_list3[-2:]



#数据转化
words=tuple(text_list2)#转换成元祖
y_pos=np.arange(len(words))#y轴词的个数
word_count=tuple(text_list3)#每个词的数量

#默认代码，可能是在初始化
plt.rcdefaults()
fig,ax = plt.subplots()

#画柱状图
ax.barh(y_pos,word_count,align='center',color='green', ecolor='black')#barh代表柱状图的方向是水平的,bar是垂直的
ax.set_yticks(y_pos)#设置y轴
ax.set_yticklabels(words,fontproperties="SimHei")#y轴标签，设置字体为黑体，不设置无法显示中文
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel(u'出现的次数',fontproperties="SimHei")#x轴标签
ax.set_title(u'张小龙演讲高频词统计',fontproperties="SimHei")#标题
plt.show()


#发邮箱的代码
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients = input('输入收件人邮箱：')
contents=text_str
subject='【自学训练营学习3群】Day13 wangzhenjia'

stmp='smtp.qq.com'

yag=yagmail.SMTP(sender,password,stmp)
yag.send(recipients,subject,contents)

