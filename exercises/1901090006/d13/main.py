import os,sys
import matplotlib.pyplot as plt
import numpy as np
# 模拟微信
from wxpy import *

# 获取当前运行脚本所在文件路径
path = os.path.dirname(os.path.abspath(__file__))

# 添加环境变量：当前脚本路径下的mymodule文件夹
sys.path.append(path+'/mymodule')

# 微信公众号下载模块，词语统计模块
import wxdownload, stats_word, wxplot

# 登陆微信
bot = Bot(cache_path = True) # 启用登陆缓存，避免重复登录封号

print('logged in, welcome', bot.self)

def plot(word_list):
	plt.rcdefaults()
	fig, ax = plt.subplots()

	# 添加中文字体
	# plt.rcParams['font.family']='sans-serif'
	# plt.rcParams['font.sans-serif'] = ['simhei']
	# plt.rcParams['axes.unicode_minus'] = False

	# 绘制图表
	word = []
	frequency = []
	for wl in word_list:
		word.append(wl[0])
		frequency.append(wl[1])

	print(word)

	y_pos = np.arange(len(word))

	ax.barh(y_pos, frequency, align='center')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(word)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Frequency')
	ax.set_title('123')

	img_name = 'word_frenquency_chart.jpg'
	plt.savefig(img_name)
	img_path = os.path.abspath(img_name)

	# plt.show()

	return img_path

# 注册监听分享类型消息
@bot.register(msg_types = SHARING)
def forward_msg(msg):
	print('you have a new message from %s:' % (msg.sender))

	# 获取分享文章内容
	content = wxdownload.download_article(msg.url)
	
	# 统计词频
	word_list = stats_word.stats_text(content,10)
	print("word:",word_list)

	# 转译成图表,保存为图片于默认路径
	x,y = [],[]
	for w in word_list:
		x.append(w[1]) # 词语y轴
		y.append(w[0]) # 频率x轴

	img_path = wxplot.plot(x,y)

	# 把图片回复给发消息的人
	msg.reply_image(img_path)


# 堵塞线程以保持监听状态，不启用控制台交互
bot.join()