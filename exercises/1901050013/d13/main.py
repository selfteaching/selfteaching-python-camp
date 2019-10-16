import requests
from pyquery import PyQuery
from mymodule.stats_word import stats_text_cn
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
from os import path



def generate_image(result, image_path):
    words = [i[0] for i in result]
    counts = [i[1] for i in result]
    print('words ===', words)
    print('counts ===', counts)
    fig = plt.figure()
    plt.grid(False)
        
    plt.rcdefaults()
    plt.rcParams['font.sans-serif'] = ['SimHei']

    fig, ax = plt.subplots()
    y_pos = np.arange(len(words))
        
    ax.barh(y_pos,counts,align='center',color="blue",ecolor="black")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    ax.set_ylabel('关键词')
    ax.set_xlabel('词频')
    ax.set_title('词频统计') 
    plt.savefig(image_path,bbox_inches='tight')  
    # plt.show() 

    

cwd = path.abspath(path.dirname(__file__))

bot = Bot() # log in the wechat.
my_friend = bot.friends() #choose all the friends.
@bot.register(my_friend,SHARING) # collecting the sharing from friends.
def auto_reply(msg): # define how to reply to the friends.
    response = requests.get(msg.url) # acquire the article link.
    document = PyQuery(response.text)
    content = document('#js_content').text() #acquire the article content.
    result = stats_text_cn(content) #convert the list type into string type.
    print(result)
    image_path = path.join(cwd, 'day13.png')
    generate_image(result,image_path)
    msg.reply_image(image_path)


embed() #keep collecting the sharing from friends.






