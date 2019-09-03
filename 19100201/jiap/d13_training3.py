# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

import requests
from pyquery import PyQuery
from mymodule import stats_word

from wxpy import *

bot = Bot()
my_friend = bot.friends()

@bot.register(my_friend)
def reply_my_friend(msg):
	if msg.type == "Sharing":
		response = requests.get(msg.url)
		document = PyQuery(response.text) 
		content = document('#js_content').text()

		frequency = stats_word.stats_text_en(content, 20)

		data = {}
		for i in frequency:
			data[i[0]] = i[1]

		x = [key for key in data.keys()]
		y = [values for values in data.values()]

		plt.rcdefaults()
		fig, ax = plt.subplots()

		ax.bar(x, y, align='center',
		        color='green', ecolor='black')

		ax.set_xlabel('Words')
		ax.set_ylabel('Numbers')
		ax.set_title('Statistics')

		plt.show()
		plt.savefig('wordcloud.png') 
		msg.sender.send_image('wordcloud.png') 

