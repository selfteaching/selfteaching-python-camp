import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties 

import numpy as np

import stats_word

import requests

from pyquery import PyQuery

from wxpy import Bot,ensure_one,SHARING,embed



def main():
    bot = Bot() 

    my_friend = ensure_one(bot.friends().search('果果爸爸')) 



    @bot.register(my_friend,SHARING) 

    def auto_reply(msg):

        response = requests.get(msg.url) #msg.url为分享的网址

        document = PyQuery(response.text)

        content = document('#js_content').text()

        

        contents = stats_word.stats_text_cn(content,count=10)

        

        result=np.array(contents) 

        word_list=[] 

        number_list=[] 

        for i in range(len(result)): 

            word_list+=[result[i][0]]

            
            number_list+=[int(result[i][1])]

        

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



    embed() #堵塞线程，保持监听状态



if __name__ == '__main__':

    main()