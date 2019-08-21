from mymodule import stats_word
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import requests
import pyquery
import wxpy 

bot = wxpy.Bot()
my_friend = bot.friends().search()
@bot.register()
def print_others(msg):
    print(msg)

@bot.register(my_friend,msg_types='Sharing') #接受分享类消息
def auto_reply(msg):
        response = requests.get(msg.url) #msg.url为分享的网址
        document = pyquery.PyQuery(response.text)
        content = document('#js_content').text()
        #处理文本
        result =stats_word.stats_text_cn(content,30)
        # Fixing random state for reproducibility
        np_list=np.array(result) #将文本处理结果转化为二维数组
        word_list=[] #初始化盛放词的列表
        number_list=[] #初始化盛放词频的列表
        for i in range(len(np_list)): #拆分Numpy多维数组
            word_list+=[np_list[i][0]]
            #Numpy在处理('a',8)的时候，会把8记录为'8'，所以需要强制转换类型为int
            number_list+=[int(np_list[i][1])]

        #绘图：
        #为了能在matplotlib中显示中文，需要中文字体的支持
        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=8)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        y_pos = np.arange(len(word_list))

        ax.barh(y_pos, number_list, align='center', color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(word_list, fontproperties=font)
        ax.invert_yaxis()
        ax.set_xlabel('词频', fontproperties=font)
        ax.set_title('好友分享文章词频统计', fontproperties=font)
        plt.savefig("stats.png") #保存图片
        msg.reply_image("stats.png") #回复图片

wxpy.embed()