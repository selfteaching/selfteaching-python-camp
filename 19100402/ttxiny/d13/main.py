import sys
sys.path.append('/anaconda3/lib/python3.7/site-packages')
from mymodule import stats_word
import requests
import pyquery
import yagmail
import getpass
from pyquery import PyQuery
from wxpy import*
import numpy as np
import matplotlib.pyplot as plt

bot=Bot()
my_friend=bot.friends().search('没没')

@bot.register(my_friends,SHARING)

def friend_sharing(msg):
    address=msg.url
    reponse=requests.get(address)
    document=PyQuery(reponse.text)
    content=document('#js_content').text()
    text1={}
    text1=dict(stats_word.stats_cn(content,20))
    np_list=np.array(text1)
    word_list=[]
    number_list=[]
    for i in range(len(np_list)):
        word_list+=[np_list[i][0]]
        number_list+=[int(np_list[i][1])]
    plt.rcdefaults()
    axis=plt.subplot()

    y_pos=np.arange(len(word_list))
    axis.barh(y_pos,number_list,align='center',color='green',ecolor='black')
    axis.set_yticks(y_pos)
    aix.set_yticklabels(word_list)
    axis.invert_yaxis()
    axis.set_xlabel('词频')
    axis.set_title('分享文章词频')
    plt.savefig('stats.png')
    msg.reply_image('stas.png')
    
embed()
