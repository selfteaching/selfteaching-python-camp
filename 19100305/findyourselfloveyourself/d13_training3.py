import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
import requests
from pyquery import PyQuery
from mymodule import stats_word
from wxpy import Bot,Message,embed

def main():
    bot = Bot() #登录微信的命令
    my_friend = bot.friends() #发给所有好友

    @bot.register(my_friend,)

    def auto_reply(msg):
            response = requests.get(msg.url)
            document = PyQuery(response.text)
            content = document('#js_content').text()
           
            result=stats_word.stats_text_cn(content,count=30)
            np_list=np.array(result)
            word_list=[]
            number_list=[]
            for i in range(len(np_list)):
                word_list+=[np_list[i][0]]
                number_list+=[int(np_list[i][1])]
            
            #为了能在matplotlib中显示中文，需要中文字体的支持
            font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=8)
            
            plt.rcdefaults()
            fig,ax=plt.subplots()
            y_pos=np.arange(len(word_list))

            ax.barh(y_pos,number_list,align='center',color='green',ecolor='black')
            ax.set_yticks(y_pos)
            ax.set_yticklabels(word_list,fontproperties=font)
            ax.invert_yaxis()
            ax.set_xlabel('词频',fontproperties=font)
            ax.set_title('词频统计',fontproperties=font)
            plt.savefig("stats.png")
            msg.reply_image("stats.png")
            
       
    embed() #保持监听状态

if __name__=='__main__':
    main()