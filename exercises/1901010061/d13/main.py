import requests
from pyquery import PyQuery
import stats_word
from wxpy import Bot,Message,embed
import matplotlib.pyplot as plt
import numpy as np
#初始化机器人，扫码登陆
bot = Bot()
#找到好友
my_friend = bot.friends().search('xx')[0]
#发送文本给好友
my_friend.send('分享任意微信文章给我')
#监听消息
#回复my_friend的消息
@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        reply = stats_word.stats_text_cn(content,10)
        r_dic = dict(reply) #字典化
        keys,values = zip(*r_dic.items()) #拆分单词和统计字数       
        np.random.seed(19680801)
        plt.rcdefaults()
        fig, ax = plt.subplots()
        
        # Example data
        people = reply
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))
        word_frequency = values

        plt.rcParams['font.sans-serif']=['SimHei'] 
        ax.barh(y_pos, word_frequency, xerr=error, align='center',color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys)
        ax.invert_yaxis()  
        ax.set_xlabel('次数')
        ax.set_title('文章高频词统计如下')
     
        plt.savefig('day13.png')
        msg.reply_image('day13.png') 
   
embed()

                
