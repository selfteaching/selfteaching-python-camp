import logging
import requests
import pyquery 
import matplotlib.pyplot as plt
from wxpy import *
from mymodule import stats_word
import numpy as np

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|%(message)s',level=logging.DEBUG)

def get_artical(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text() 

def main():

    bot = Bot()
    my_friend = bot.friends()
    @bot.register(my_friend,SHARING)
    def handler(msg):
        try:
            logging.info('Sharing url = %s',msg.url)
            artical = get_artical(msg.url)
            result = stats_word.stats_text_cn(artical,10)
            result_dic = dict(result)
            keys,values = zip(*result_dic.items())
            
            plt.rcdefaults()
            fig, ax = plt.subplots()
            y_pos = np.arange(len(keys))
            word_frequency = values
            plt.rcParams['font.sans-serif']=['SimHei'] 
            ax.barh(y_pos, word_frequency, align='center',color='red', ecolor='black')
            ax.set_yticks(y_pos)
            ax.set_yticklabels(keys)
            ax.invert_yaxis()  
            ax.set_xlabel('Frequency')
            ax.set_title('文章高频词统计') 
            plt.savefig('stats.png')
            msg.reply_image('stats.png')
        except Exception as e:
            logging.exception(e)    
    embed()


if __name__ =='__main__':
    main()