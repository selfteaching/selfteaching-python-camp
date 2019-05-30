import matplotlib
matplotlib.use('TkAgg')
import json
import stats_word
import jieba
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import _rebuild

_rebuild()
bot = Bot()
my_friend = bot.friends().search('Isabelmima')[0]
@bot.register(my_friend, SHARING)
def wxpy_stats_word(Message):
        message_url = Message.url
        response = requests.get(message_url)
        document = PyQuery(response.text) 
        content = document('#js_content').text()
        contents = stats_word.stats_text_cn(content,5)
        words = [item[0] for item in contents]
        frequency = [item[1] for item in contents]

        plt.rcdefaults()
        fig, ax = plt.subplots()
        y_pos = np.arange(len(words))
        ax.barh(y_pos, frequency, align='center', color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words, Fontproperties ='STHEITI')
        ax.invert_yaxis()  
        ax.set_xlabel('Frequency')
        ax.set_title('Word Frequency')
        plt.savefig('/Users/maminyi/Desktop/word_frequency.png')
        
        my_friend.send_image('/Users/maminyi/Desktop/word_frequency.png')

embed()