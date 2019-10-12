# this is d12 exercise for using wxpy
# date: 2019.10.6
# author by: rtgong

import logging
import requests
import pyquery
import logging
import matplotlib.pyplot as plt
import numpy as np
from mymodule import stats_word
from wxpy import *

logging.basicConfig(format='file:%(filename)s|line:%(lineno)s|message:%(message)s',level=logging.DEBUG)

def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()

def main():
    bot = Bot()
    friends = bot.friends()
    
    @bot.register(friends,SHARING)
    def handler(chart):
        try:
            logging.info('sharing url = %s', chart.url)
            article = get_article(chart.url)
            result = stats_word.stats_text_cn(article,10)
            plt.rcdefaults()
            fig, ax = plt.subplots()
            words = [result]
            y_pos = np.arange(len(words))
            number = 3 + 10 * np.random.rand(len(words))
            error = np.random.rand(len(words))

            ax.barh(y_pos,number, xerr=error, align='center')
            ax.set_yticks(y_pos)
            ax.invert_yaxis()
            ax.set_xlabel('Number')
            ax.set_title('The top 10 words in the article')

            chart.reply(plt.show(result))
        except Exception as e:
            logging.exception(e)
    embed

if __name__=="__main__":
    main()
