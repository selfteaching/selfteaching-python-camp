#将实战项⽬目1的功能包装集成到个⼈人微信
'''from wxpy import *
bot = Bot()
my_friend=bot.friends()
@bot.register(my_friend,SHARING)
def get_friend_url(msg):
    if isinstance(msg.type,SHARING):
        import requests
        response=requests.get(msg.url)
        from pyquery import PyQuery
        document=PyQuery(response.text)
        content=document('#js_content').text()
        from stats_word import stats_text_cn
        body=str(stats_text_cn(content))
        msg.reply(body)
embed()
'''
#Day11作业转化成图表
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
from pyquery import PyQuery
document=PyQuery(response.text)
content=document('#js_content').text()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pylab import mpl
mpl.rcParams['font.sans-serif']=['Microsoft YaHei']

from stats_word import stats_text_cn
data=stats_text_cn(content)
group_data=list(data.values())
group_names=list(data.keys())

plt.rcParams.update({'figure.autolayout':True})
fig,ax=plt.subplots()
ax.barh(group_names,group_data)
plt.style.use('seaborn-paper')
labels=ax.get_xticklabels()
plt.setp(labels,horizontalalignment='right')
ax.set(xlabel='词频',ylabel='中文汉字',title='中文汉字词频统计')
plt.show()





