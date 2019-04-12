# -*- encoding: utf-8 -*-
import requests
from pyquery import PyQuery 

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
my_friend = bot.friends()

@bot.register(my_friend)
def reply_my_friend(msg):
	if msg.type == "Sharing":
		print('1')
		print(msg.url)

		response = requests.get(msg.url)
		document = PyQuery(response.text) 
		content = document('#js_content').text()

		return content


# embed()