import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as mfm
from mymodule import stats_word 
import  requests
from pyquery import PyQuery
from wxpy import *

font = mfm.FontProperties(fname='/System/Library/Fonts/huizi.ttc')


# 初始化机器人，扫码登陆
bot = Bot()

my_friends = bot.friends().search('慧子')[0]

# 获取文章url
@bot.register(my_friends,SHARING)
def get_msg (msg) :
    #使用requests获得获得网络链接的文本
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()

    #提取高频词汇统计
        content1= stats_word.stats_text_cn(content,100)

        # 拆分
        data = dict(content1)
        keys, values = zip(*data.items())

        plt.rcdefaults()
        fig, ax = plt.subplots()

        #图表制作
        people = (content1)
        y_pos = np.arange(len(content1))
        cipin = values
        
        # 绘制图表
        ax.barh(y_pos, cipin, align='center',color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys,fontproperties=font)
        ax.invert_yaxis()  # labels read top-to-bottom
        
        # 自定义表格标签及标题样式
        ax.set_xlabel('词频',fontproperties=font, color = 'grey')
        ax.set_ylabel('词语',fontproperties = font, color = 'grey')
        ax.set_title('文章词频查询结果',fontproperties=font)

        plt.savefig('day13.png')

        #给好友发送信息
        my_friends.send('day13.png')

embed()    # 

