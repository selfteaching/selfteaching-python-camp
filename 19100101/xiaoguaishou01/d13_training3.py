import matplotlib.pyplot as plt
import numpy as np
from mymodule import stats_word
from wxpy import Bot,Message,embed
import d11_training1

bot = Bot()
@bot.register()
def print_others(msg):
    '''1、如果消息是Sharing类型，获取URL并对文本进行统计，输出前100的词频'''
    if msg.type == 'Sharing':#如果是sharing类型
        result_url = d11_training1.auto_text(msg.url)
        plt.rcParams['font.sans-serif']=['SimHei']
        for i in result_url:
            for j in result_url[i]:
                plt.barh((j[0]),(j[1]))
        plt.title('词频(Top-20)')
        plt.xlabel('词频')
        plt.ylabel('单词')
        plt.legend('词频二维图')
        #plt.show()
        plt.savefig('filename.png')
        msg.reply_image('filename.png')#发送result的内容给好友
        #msg.reply(result_url)
embed()     