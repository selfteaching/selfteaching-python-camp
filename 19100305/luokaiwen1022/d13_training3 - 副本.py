import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig,ax = plt.subplots()

def matplt (Xname,Ynum):
    y_pop = range(len(Ynum))

    ax.bar(y_pop, Ynum,tick_label=Xname,align='center',
        color='green', ecolor='black')
    ax.set_ylabel('CIPIN')
    ax.set_xlabel('CIHUI')
    ax.set_title('WEN ZHANG FAN KUI：')

    plt.savefig('C:/Users/admin/frcy.png')
    plt.show()
    
from wxpy import *

bot = Bot(cache_path=True)

my_friend = bot.friends()

@bot.register(my_friend)

def get_msg(msg):
    if msg.type == 'Sharing':
      target = msg.url

      import requests
      import yagmail
      import getpass
      from pyquery import PyQuery
      from mymodule import stats_word
      
      response = requests.get('target')

      document = PyQuery (response.text)
      content = document ('#js_content').text() 

      statList = stats_word.stats_text(content,5)
      
      print(statList)

      cipin_list=[]
      cihui_list=[]
      for i in statList:
          cihui_list.append(i[0])
          cipin_list.append(i[1])
          print(cihui_list)
      matplt(cihui_list,cipin_list)
      my_friend.send_image('C:/Users/admin/frcy.png')


embed()