import requests
import pyquery
import yagmail
import getpass
from pyquery import PyQuery
import stats_word
from wxpy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.font_manager import FontProperties
#扫码登录微信
bot = Bot() 
	
# 查找朋友:
my_friend=bot.friends().search('蓝溪')[0] #查找好友变量
	
#自动回复
@bot.register(my_friend)
def auto_reply_my_friend(msg):
	return 'received:{}({})'.format(msg.text,msg.type)
	
# 发送文本和图片给好友
my_friend.send('请发一篇分享文章')
	
#监听朋友信息
@bot.register(my_friend)
def print_others(msg):
	print(msg) 
	
#监听朋友分享的信息,自动回复统计数据和图表
@bot.register(my_friend,SHARING) #接收sharing类信息
def auto_reply(msg):
	sharing_text = requests.get(msg.url)  
	document = PyQuery(sharing_text.text)
	content = document('#js_content').text()
	
	import numpy as np                         #调用numpy 库函数
	import matplotlib.pyplot as plt             #调用matplotlib 库函数
	from matplotlib.ticker import FuncFormatter
	
	l1=stats_word.stats_text_cn(content,count=10)      ##统计微信消息前10位热词
	data=dict(l1)                                  #将统计结果热词数据字典化
	group_data = list(data.values())
	group_names = list(data.keys())
	group_mean = np.mean(group_data)
	
	plt.rcParams['font.sans-serif']=['SimHei']     # 统计表格数据格式汉化
	
	fig, ax = plt.subplots(figsize=(8, 8))          #使用plt模版导入数据生成图表
	ax.barh(group_names, group_data)
	labels = ax.get_xticklabels()
	plt.setp(labels, rotation=45, horizontalalignment='right')
	ax.set(xlim=[0, 50], xlabel='词频( 次 )', ylabel=' 热词 ',title='热词词频统计')
	plt.show()
	fig.savefig('热词词频统计表.png')  # 将统计图表存成png格式
	my_friend.send_image('热词词频统计表.png')   #发送统计结果图片
	result = stats_word.stats_text_cn(content,count=10) #统计热词
	return result #将热词自动回复给好友 
#让程序保持运行 
embed()	