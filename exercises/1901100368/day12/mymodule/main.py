import stats_word
import getpass
import requests
from pyquery import PyQuery as pq
from wxpy import *
'''
bot = Bot() #扫描二维码登录微信
my_friend = bot.friends() #回复对象为所有好友

@bot.register(my_friend,SHARING) #接受分享类消息
def auto_reply(msg):
    response = requests.get(msg.url) #msg.url为分享的网址
    document = PyQuery(response.text)
    content = document('#js_content').text()
    #处理文本
    result = stats_word.stats_text_cn(content,count=100)
    return result #将结果返回给好友

embed() #堵塞线程，保持监听状态
'''

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()