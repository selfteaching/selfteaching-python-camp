
# 导入模块
import matplotlib.pyplot as plt
import numpy as np
from wxpy import *
from mymodule import stats_word
from pyquery import PyQuery
import requests

'''
1、调用day12方法，获取统计结果
2、将结果导入day13处理，并生成图片
3、将图片传回day12，并发给朋友
'''

import matplotlib.font_manager as mfm

font = mfm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


# 初始化机器人，扫码登陆
bot = Bot()

'''
my_friend = bot.friends().search('亲宝儿')[0]  # 测试用
my_friend.send('给我分享篇文章试下')
'''

@bot.register(my_friend)
def print_others(msg):
    print (msg.type)
    if msg.type =='Sharing':
        
        response = requests.get(msg.url)    # 请求获得内容

        document = PyQuery(response.text)    # 解析提出内容
        content = document('#js_content').text()

        result = stats_word.stats_text(content)
        content1 = result.most_common(20)
        day12 = str(content1)
        print(day12)

        # 拆分
        data = dict(content1)
        keys, values = zip(*data.items())

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = (content1)
        y_pos = np.arange(len(content1))
        cipin = values

        ax.barh(y_pos, cipin, align='center',color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys,fontproperties=font)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('词频',fontproperties=font)
        ax.set_title('文章词频查询结果',fontproperties=font)

        plt.savefig('day13.png')
        msg.reply_image('day13.png')

embed()    # 让程序保持运行

