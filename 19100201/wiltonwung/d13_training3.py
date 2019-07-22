import matplotlib.pyplot as plt
import numpy as np

import requests
from pyquery import PyQuery
from mymodule import stats_word

from wxpy import *

bot = Bot() 

my_friend = bot.friends()

@bot.register(my_friend)

def SHARING_Msg(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text) 
        content = document('#js_content').text()  
        c= stats_word.stats_text(content, 10)
        d = visualized(c)
        msg.reply_image(d)
    else:
        print('waiting......')

embed()
        

def visualized(data={}):
    data_x = list(data.values())
    data_y = list(data.keys())
   
    plt.title('words&frequency')
    ax.set_xlabel('frequency')
    ax.set_ylabel('words')
    fig, ax = plt.subplots()
  
    ax.set_yticklabels(data_y)
    ax.barh(data_y, data_x)
    ax.invert_yaxis() 
 
    plt.savefig('chart.png')
return 'chart.png'


