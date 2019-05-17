from pyquery import PyQuery as pq
import requests
from mymodule import stats_word
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

def main():
        bot = Bot(console_qr=True)
        my_friend = bot.friends().search('QQ')[0]
        my_friend.send('你好！')

        @bot.register(my_friend)
        def step1(msg):
                print(msg.url)
                if msg.type == 'Sharing':
                        response = requests.get(msg.url)
                        document = pq(response.text)
                        content = document('#js_content').text()
                        result = stats_word.stats_text_cn(content,20)

                        words = []
                        count = []
                
                        for i in result:
                                words.append(i[0])
                                count.append(i[1])
                
                        np.random.seed(19680801)
                        plt.rcdefaults()
                        fig,ax = plt.subplots()
                        font = FontProperties(fname=r"/Library/Fonts/Songti.ttc", size=8)

                        y_pos = np.arange(len(words))
                        error = np.random.rand(len(words))
                        ax.barh(y_pos,count,xerr=error,align='center',color='green',ecolor='black')
                        ax.set_yticks(y_pos)
                        ax.set_yticklabels(words,fontproperties=font)
                        ax.invert_yaxis()
                        ax.set_xlabel('次数',fontproperties=font)
                        ax.set_title('朋友所分享的文章中出现最多的20个词',fontproperties=font)
                        plt.savefig('stats.png')
                        msg.reply_image('stats.png')
        embed()

if __name__ == '__main__':
        main()
