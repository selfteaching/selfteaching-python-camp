

import yagmail
import requests
import getpass
from pyquery import PyQuery
from mymodule.stats_word import stats_text_cn

def main():
	#获取网页内容
	response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
	document = PyQuery(response.text)
	content = document('#js_content').text()
	#处理文本
	result = stats_text_cn(content,count=100)
	#登录邮箱并发送结果
	sender = input('Please input your email address:')
	password = getpass.getpass('Please input your password:')
	recipients = input('Please input the recipients:')
	title = input('Please input the title:')
	yag = yagmail.SMTP(sender,password,'smtp.aliyun.com')
	yag.send(to=recipients,subject=title,contents=str(result))

	
main()






