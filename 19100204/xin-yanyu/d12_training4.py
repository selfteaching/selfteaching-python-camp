# 第12天作业
# 2019年4月01日
# 1.在文件中引入wxpy模块；
# 2.监听好友消息，
# 3.如果消息为分享（sharing）类型的消息，则获取消息的网页链接（msg.url）；
# 4.将获取的链接使用：
# （1）通过网络请求获得网页内容，
# （2）使用分词工具对中文字符串进行分词，
# （3）统计词频，得出结果，
# 5.将处理结果返回给发消息的好友
# 6.使用另一个个人的微信分享一篇公众号文章给登录微信机器人的个人微信号。 


try :
	import stats_word
except :
	print('stats_word.py模块不在当前目录,程序出错退出')
	exit()
	
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
	

# 导入模块
from wxpy import *
bot = Bot()
#bot = Bot(cache_path=True)
my_friend = bot.friends().search('yywww')[0]

# 发送文本给好友
my_friend.send('严雨的自学能力太强大了！')


# 回复 my_friend 发送的消息 
@bot.register(my_friend) 
def reply_my_friend(msg): 
	#如果消息为分享（sharing）类型的消息，则获取消息的网页链接（msg.url）
	print(msg)
	if msg.type== 'Sharing' :
		my_friend_msg_url=msg.url
		#将获取的链接通过网络请求获得网页内容
		#print(my_friend_msg_url)
		text_str=(requests_weixin(my_friend_msg_url))
		#print(text_str)
		#调用stats_word模块中的stats_text函数，统计词频
		# int _num词频统计数
		int_num=100
		#print(int_num)
		#使用分词工具对中文字符串进行分词，统计词频，得出结果，
		#print('微信分享文章的词频分析，前100个词和词频数为：')
		text_num_100 = stats_word.stats_text(text_str,int_num)
		print(text_num_100)

		# 将处理结果返回给发消息的好友
		#msg.reply_my_friend
		return  '微信分享文章的词频分析，前100个词和词频数为： {} '.format(text_num_100)
        #(text_num_100)

# 进入 Python 命令行、让程序保持运行
embed()





