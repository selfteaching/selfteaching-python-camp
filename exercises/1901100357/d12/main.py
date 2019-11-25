#coding:utf-8
from mymodule import stats_word
import logging
import yagmail
import requests
import pyquery
import getpass
# import wxpy
from wxpy import *


logging.basicConfig(
	format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)

#提取微信公众号文章正文
def get_article():
	r = requests.get(Message.url)
	document = pyquery.PyQuery(r.text)
	return document('#js_content').text()

def main():
	try:
		article = get_article()
		result = stats_word.stats_text_cn(article, 10)
		logging.info('%s %s', type(result), str(result))
		sender = input('请输入发件人邮箱：')
		password = getpass.getpass('输入发件人邮箱密码：')
		recipients = input('请输入收件人邮箱：')
		yag = yagmail.SMTP(sender, password, 'smtp.sina.com')
		yag.send(recipients, '自学训练营', str(result))
		logging.info('已发送')
	except Exception as e:
		logging.exception(e)

bot = Bot()
# my_friend = bot.friends()

# embed()
if Message.type == SHARING:
	article = get_article()
	result = stats_word.stats_text_cn(article, 10)
	Message.reply_msg(Message.sender, result)






# if __name__ == "__main__":
# 	main()
	