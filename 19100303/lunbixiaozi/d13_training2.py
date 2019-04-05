#coding:utf-8
from pyquery import PyQuery
from wxpy import *
import yagmail
import requests
import getpass
import mymodule.stats_word
import matplotlib.pyplot as plt
from matplotlib.font_manager import *

import matplotlib
matplotlib.matplotlib_fname() #将会获得matplotlib包所在文件夹
import numpy as np
from matplotlib.font_manager import _rebuild
_rebuild()
pic_path = 'C:\\Users\\flami\Documents\\GitHub\\selfteaching-python-camp\\19100303\\lunbixiaozi\\'
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

myfont = FontProperties(fname='C:/ProgramData/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf')

counter_cn_dict_keys = []
counter_cn_dict_values = []
#def main():
    # bot = Bot() #扫描二维码登录微信
    # my_friend = bot.friends() #回复对象为所有好友

    # @bot.register(None,None) #接受分享类消息
    # def auto_reply(msg):
    #     # response = requests.get(msg.url) #msg.url为分享的网址
    #     # document = PyQuery(response.text)
    #     # content = document('#js_content').text()
    #     #处理文本
    #     result = 'lala' #stats_word.stats_text_cn(content,100)
    #     return result #将结果返回给好友

    # embed() #堵塞线程，保持监听状态

# if __name__ == '__main__':
#     main() 

r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',auth=('user','pass'))
document=PyQuery(r.text)
content=document('#js_content').text()

counter_cn_dict = mymodule.stats_word.stats_text_cn(content, 20)
for i in counter_cn_dict.keys(): 
    counter_cn_dict_keys.append(i)
for i in counter_cn_dict.values(): 
    counter_cn_dict_values.append(i)

###pictures:

plt.rcdefaults()
fig, ax = plt.subplots()

y_pos = np.arange(len(counter_cn_dict_keys))

ax.barh(y_pos, counter_cn_dict_values, align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(counter_cn_dict_keys, fontproperties=myfont)
ax.invert_yaxis()
ax.set_xlabel('Counts')
ax.set_title('词频统计', fontproperties=myfont)
plt.savefig(pic_path + 'frequency.jpg')
plt.show()
# print(counter_ke)
#counter_cn_string = str(counter_cn_dict)



'''
bot = Bot()
myself = bot.self
bot.file_helper.send('Hello from wxpy!')

@bot.register()
def print_messages(msg):
    if msg.type == SHARING:
        r=requests.get(msg.url,auth=('user','pass')) 
        document=PyQuery(r.text)
        content=document('#js_content').text()
        counter_cn_dict = mymodule.stats_word.stats_text_cn(content, 100)
        counter_cn_string = str(counter_cn_dict)
        msg.reply(counter_cn_string)

embed()
'''