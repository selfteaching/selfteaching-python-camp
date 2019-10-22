# 使用另一个个人微信分享一篇文章 给登录微信机器人的个人微信号,并统计好文章词频,将处理结果返回给发送消息过来的好友

# # 导入模块
# from wxpy import *
# # 初始化机器人，扫码登陆
# bot = Bot()
# # 找到所以好友 
# my_friend = bot.friends()
# # 监听好友信息，自动响应分享类型的消息
# @bot.register(my_friend,SHARING)   #对于 --我的好友和其他群聊中 分享类型 SHARING的消息:
# # @bot.register([my_friend,Group],SHARING)   #对于 --我的好友和其他群聊中 分享类型 SHARING的消息:
# def get_friend_url(msg) :
#     if isinstance(msg.type,SHARING):
#         import requests
#         response=requests.get(msg.url)

#         from pyquery import PyQuery
#         document=PyQuery(response.text)
#         content=document('#js_content').text()

#         from mymodule import stats_word  
#         email_content = str(stats_word.stats_text_cn(content))

#         msg.reply(email_content)
#         # print ("我的好友或群里成员 分享的内容,转化为从大到小的词频为 >>>" + email_content)
# # 进入 Python 命令行、让程序保持运行
# embed()


#转化成图表
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
document=PyQuery(response.text)
content=document('#js_content').text()

###############################################
import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
plt.rcdefaults()
fig, ax = plt.subplots()

from matplotlib.ticker import FuncFormatter
from pylab import mpl
mpl.rcParams['font.sans-serif']=['Microsoft YaHei']
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

###################################################

from mymodule import stats_word
email_content = stats_word.stats_text_cn(content)
print (email_content)    # data 是一个大字典

key_s = list(email_content.keys())   # 对大字典操作分别取出 键和值(操作后默认是元组类型,再用list()转换为列表)
value_s = list(email_content.values())  # 对大字典操作分别取出 键和值(操作后默认是元组类型,再用list()转换为列表)

# print(f"vakue_s的类型为: {type(value_s)}")
# print (f"词频中所有的 词_键 为: {key_s}")
# print (f"词频中所有的词 词频_值 为: {value_s}")

y_pos = np.arange(len(key_s)) 
# performance =  value_s
error = np.random.rand(len(key_s))


ax.barh( y_pos, value_s, xerr=error, align='center')
ax.set_yticks(y_pos)       # y轴元素名
ax.set_yticklabels(key_s)  # y轴标签
ax.invert_yaxis()           
ax.set_xlabel('词频')    # X轴标签
ax.set_title('中文汉字词频统计') # 图标名
plt.savefig('作业 微信文章词频统计',dpi = 600)   # 保存图像,dpi图像像素质量

plt.show()

