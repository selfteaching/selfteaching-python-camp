import stats_word
import getpass
import requests
from pyquery import PyQuery as pq
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties #为了显示中文，替换字体

#bot = Bot() #扫描二维码登录微信（微信无法使用，仅做绘图）
#my_friend = bot.friends() #回复对象为所有好友（微信无法使用，仅做绘图）

#@bot.register(my_friend,SHARING) #接受分享类消息（微信无法使用，仅做绘图）
#def auto_reply(msg):
#    response = requests.get(msg.url) #msg.url为分享的网址（微信无法使用，仅做绘图）
#    document = PyQuery(response.text)#msg.url为分享的网址（微信无法使用，仅做绘图）
#    content = document('#js_content').text()#msg.url为分享的网址（微信无法使用，仅做绘图）
    #处理文本

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = pq(response.text)
content = document('#js_content').text()
result = stats_word.stats_text_cn(content,15)
np_list=np.array(result) 
word_list=[] 
number_list=[]
list_A = []
list_B = []
for i in range(len(np_list)): 
    word_list+=[np_list[i][0]]
    number_list+=[int(np_list[i][1])]
for i in range(len(word_list)): 
    list_A+=[word_list[i][0]]
    list_B+=[int(word_list[i][1])]
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=8)
plt.rcdefaults()
fig, ax = plt.subplots()
y_pos = np.arange(len(list_A))
ax.barh(y_pos, list_B, align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(list_A, fontproperties=font)
ax.invert_yaxis()
ax.set_xlabel('词频', fontproperties=font)
ax.set_title('词频统计', fontproperties=font)
plt.savefig("result.png") 
#embed() #堵塞线程，保持监听状态
