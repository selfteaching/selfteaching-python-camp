import matplotlib.pyplot as plt
import numpy as np
from wxpy import *

bot = Bot(console_qr=True,cache_path=True) 

my_friend = bot.friends() 

@bot.register(my_friend,SHARING) 

def auto(msg):
    text = msg.url
    import requests
    response = requests.get(text) 
    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text()
    WORD=Chinesechar(content)
    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    words = (WORD[0][0], WORD[1][0], WORD[2][0], WORD[3][0], WORD[4][0])
    y_pos = np.arange(len(words))
    times = (WORD[0][1],WORD[1][1],WORD[2][1],WORD[3][1],WORD[4][1])
    error = np.random.rand(len(words))
    ax.barh(y_pos, times, xerr=error, align='center',color='blue', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('times')
    ax.set_title('The most words in the title')
    plt.show()
    plt.savefig("C:/Users/Administrator/cipin.png")
    msg.sender.send_image("cipin.png")

embed()
