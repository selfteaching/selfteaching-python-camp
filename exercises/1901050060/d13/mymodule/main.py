import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np

bot = Bot()
@bot.register()
def print_others(msg):
    '''1、先判断消息是Sharing类型，获取URL并对文本进行统计，输出前100的词频'''
    if msg.type == 'Sharing':#如果是sharing类型
        response = requests.get(msg.url)#msg.url为分享的网址
        document = PyQuery(response.text)
        content = document('#js_content').text()
        #结巴处理
        result = stats_word.stast_text_cn(content,count=10)
        result_dict = dict(result)
        word = []
        number = []
        for i in result_dict:
            word.append(i)
            number.append(result_dict[i])
        plt.rcdefaults()
        fig, ax = plt.subplots()
        y = np.arange(len(word))
        error = np.random.rand(len(word))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 将中文字体显现
        ax.barh(y, number, xerr=error, align='center', color='red')
        ax.set_yticks(y)
        ax.set_yticklabels(word)
        ax.invert_yaxis()
        ax.set_xlabel('出现次数')
        ax.set_title('词频统计表')
        plt.savefig('day13.png')
        msg.reply_image('day13.png')


embed()

