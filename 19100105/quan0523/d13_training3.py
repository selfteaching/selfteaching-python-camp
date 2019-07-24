import requests
from pyquery import PyQuery
import mymodule.stats_word
from wxpy import *

import matplotlib.pyplot as plt
import numpy as np

# 'https://segmentfault.com/a/1190000005144275'
plt.rcParams['font.sans-serif']=['SimHei']   # 用来正常显示中文标签
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus']=False   # 用来正常显示负号

bot = Bot()

my_friend = bot.friends().search('权')[0]    # 找到好友
my_friend.send('send me something')    # 发送消息给这个好友

@bot.register(my_friend)
def reply_my_friend(msg):
    print(msg)
    if msg.type =='Sharing':    # 如果是公众号内容进行统计词频处理
        response = requests.get(msg.url)    # 请求获得内容
        document = PyQuery(response.text)    # 解析提出内容
        content = document('#js_content').text()
        #print(content)
        result = mymodule.stats_word.stats_text_cn(content)    # 导入公式处理结果

        cizu=[]
        cipin=[]
        for x in result:
            cizu.append(x[0])
            cipin.append(x[1])

        plt.rcdefaults()
        fig,ax = plt.subplots()
        people = cizu
        y_pos = np.arange(len(people)) 
        performance = np.array(cipin)
        ax.barh(y_pos, performance, align='center',
        color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('词汇')
        ax.set_ylabel('词频')
        ax.set_title('词频统计结果')
        plt.savefig('C:/Users/admin/test.png')
        # plt.show()  加入这串文档示范的代码会让图片无法发送，why？
        
        # my_friend.send(str(result))    # 文字结果发送给好友
        my_friend.send_image('C:/Users/admin/test.png')    # 发送图片结果
    else:
        pass
    
embed()    # 让程序保持运行