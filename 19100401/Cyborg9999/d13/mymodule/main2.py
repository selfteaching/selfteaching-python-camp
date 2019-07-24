import matplotlib.pyplot as plt
import numpy as np
import stats_word
from wxpy import *
import main

bot = Bot(console_qr=True,cache_path=True)
@bot.register()
def print_others(msg):
    if msg.type == 'Sharing':
        result = main.stats(msg.url)
        plt.rcParams['font.sans-serif']=['SimHei']
        for i in result:
            for j in result[i]:
                plt.barh((j[0]),(j[1]))
        plt.title('词频(Top-20)')
        plt.xlabel('词频')
        plt.ylabel('单词')
        plt.legend('词频二维图')
        plt.savefig('filename.png')
        msg.sender.send_image('filename.png')
        plt.show()
        
embed()     