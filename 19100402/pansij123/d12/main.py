from modules.stats_word import stats_text_cn as st
import json
from pyquery import PyQuery as pq
import requests as rq
from wxpy import *

bot=Bot()
friends=bot.friends()

@bot.register(friends)

def action(m):
	if m.type == 'Sharing' :
		r=rq.get(m.url)
		q=pq(r.text)
		t=q('#js_content').text()
		print(type(t))
		print(t)

		#-stat words- in t#
		print("Statting cn words...")
		try:
			s = st(t,101)
			#print(s[1:100])
			print(type(s))
			string = ''
			for i in s:
				string+=(str(i))
			print(string)
			print(type(string))
			return s #equivlent to msg.reply m.reply
		except TypeError:
			print("\nFrom main.py:\tInput should be string if you see an error above")
embed()
