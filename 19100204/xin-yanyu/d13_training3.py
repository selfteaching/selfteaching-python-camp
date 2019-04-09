# 第13天作业
# 2019年4月02日
# 1.将在微信中收到的词频结果生成一张图片图片文件
# 2.用图表图片文件替代之前发送的文本发给好友。


def requests_weixin(url_weixin) :
	''' 使用requests请求微信公众号文章的链接，
	获取返回结果，
	用pyquery把正文提取出来
	参数：网址
	返回chr格式的正文
	'''
	#提取微信公众号文章
	import requests
	response = requests.get(url_weixin)
	#提取正文
	from pyquery import PyQuery
	document = PyQuery(response.text)
	content = document('#js_content').text()
	return(content)	
	
	
def plot_text_num(str_text) :
	'''绘制词频图表
	
	输入词频字典：{'str'：num，……}
	返回柱状图片
	'''
	# 导入绘图模块
	import matplotlib.pyplot as plt
	# 构建数据,将词频字典读出来
	# x为词语
	x = []
	# y词频数
	y = []
	y_max=0
	for (x1,y1) in str_text.items():
		x.append(x1)
		y.append(y1)
		if y_max<=y1 :
			y_max=y1
		y_max = int(y_max / 10 + 1)*10
	# 中文乱码的处理
	plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
	plt.rcParams['axes.unicode_minus'] = False
	
	# 绘图
	plt.bar(x, y, align = 'center',color='purple', alpha = 0.5)
	# 添加轴标签
	plt.ylabel('词语频率')
	# 添加标题
	plt.title('微信文章词频比拼')
	# 添加刻度标签
	plt.xticks(range(10),x)
	# 设置Y轴的刻度范围
	plt.ylim([0,y_max])
	# 为每个条形图添加数值标签
	for x,y in enumerate(y):
		plt.text(x,y,'%s' %round(y,1),ha='center')
	# 保存但不显示图形
	plt.savefig('NA.png', dpi=80)
	#plt.show()
	return

try :
	import stats_word
except :
	print('stats_word.py模块不在当前目录,程序出错退出')
	exit()
	
# 导入模块
from wxpy import *
bot = Bot()
#bot = Bot(cache_path=True)
my_friend = bot.friends().search('yywww')[0]

# 发送文本给好友
my_friend.send('严雨的很厉害！')

# 回复 my_friend 发送的消息 
@bot.register(my_friend) 
def reply_my_friend(msg): 
	#如果消息为分享（sharing）类型的消息，则获取消息的网页链接（msg.url）
	if msg.type== 'Sharing' :
		my_friend_msg_url=msg.url
		#将获取的链接通过网络请求获得网页内容
		text_str=(requests_weixin(my_friend_msg_url))
		
		#调用stats_word模块中的stats_text函数，统计词频
		#使用分词工具对中文字符串进行分词，统计词频，得出结果，	
		int_num=10
		text_num_10 = stats_word.stats_text(text_str,int_num)

		#生成词频图表，并保存为图片
		plot_text_num(text_num_10)		
		
		# 将处理结果返回给发消息的好友
		msg.reply_image("NA.png") #回复图片
		#return  '微信分享文章的词频分析，前10个词和词频数为： {} '.format(text_num_10)
        
# 进入 Python 命令行、让程序保持运行
embed()





