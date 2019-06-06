from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np

bot=Bot()
my_friend=bot.friends()

@bot.register(my_friend,SHARING)

def reply_my_friend(msg):
    response=requests.get(msg.url)
    document=PyQuery(response.text)
    content=document('#js_content').text()
    reply=dict(stats_word.stats_text_cn(content,10))
    num_list=list(reply.values())
    name_list=list(reply.keys())

    fig,ax=plt.subplots()
    plt.title('Frequency summary',color='black',fontsize=16)
    ax.set_xlabel('frequency',color='grey')
    ax.set_ylabel('words',color='grey')

    ax.set_yticklabels(num_list)
    ax.barh(num_list,name_list)

    plt.savefig('words_frequency.png')
    return 'words_frequency.png'
       
embed()







    