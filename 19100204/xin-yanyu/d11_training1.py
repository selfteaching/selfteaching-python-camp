# 第11天作业
# 2019年3月31日
# 1.通过网络请求获得网页内容，
# 2.使用分词工具对中文字符串进行分词，
# 3.统计词频，得出结果，
# 4.发送到指定的邮箱
# 完善词频统计的排序功能主程序
# 

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

def email_to(text_email) :
	'''发送邮件到特定邮箱
	'''

	#输入发信人、收信人邮箱数据
	import getpass
	sender = input('输入发件人邮箱： ')
	password = getpass.getpass('输入发件人邮箱密码')
	rcipients = input('输入收件人邮箱:')
	
	#sender = '13702307706@139.com'
	#password = '**'
	#rcipients = 'pythoncamp@163.com'
	#rcipients = '13702307706@139.com'

	#发邮件
	import yagmail
	#链接邮箱服务器
	yag = yagmail.SMTP(user=sender, password=password , host='smtp.139.com')
	#邮箱正文
	# 发送邮件
	yag.send(to =rcipients, subject='19100204 xin-yanyu', contents=text_email)
	return
	
	
#读取微信公众号文章	
url='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
text_weix=(requests_weixin(url))

#调用stats_word模块中的stats_text函数，统计词频
# int _num词频统计数
int_num=100

#print(text_weix)
print('张小龙演讲词频分析，前100个词和词频数为：')
text_num_100 = stats_word.stats_text(text_weix,int_num)
print(text_num_100)
text_num_100_str=str(text_num_100)
email_to(text_num_100_str)

