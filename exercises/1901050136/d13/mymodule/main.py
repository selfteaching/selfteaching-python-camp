# this script is to implement plotting
import logging
import stats_word as s
import requests
from pyquery import PyQuery as pq
import yagmail
import wxpy
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
from os import path
from pylab import * # for chinese characters
import matplotlib
matplotlib.use('qt4agg')
from matplotlib.font_manager import *
# plt.rcParams['font.sans-serif'] = ['SimHei']

# get the current address of the file
cwd = path.abspath(path.dirname(__file__))
# # set the font of the characters
plt.rcParams['font.sans-serif'] = 'SimHei'

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s',level=logging.DEBUG)

# get the article from the wechat
def get_article(url):
    response = requests.get(url)
    document = pq(response.text)
    content = document('#js_content').text()
    return content 

def plotting(stat_result,image_path):
    # DATA FOR X AND y AXIS
    keys =[] # list for all the statis_words
    values = [] # list for the numbers for every statis_words
    keys = [ word[0] for word in stat_result ]
    values = [word[1] for word in stat_result ]
    ypos = range(len(stat_result))
    fig, ax = plt.subplots()
    ax.barh(ypos,values)
    ax.set_yticks(ypos)
    ax.set_yticklabels(keys,fontproperties = 'SimHei')
    ax.invert_yaxis()
    ax.set_ylabel('keywords')
    ax.set_xlabel('statistics')
    ax.set_title('statistics for keywords')
    plt.savefig(image_path,bbox_inches='tight')
    return None

def main():
    bot = Bot() # 
    friends = bot.friends()

    @bot.register(friends, SHARING)
    def handler(msg):
        try:
            logging.info('sharing url - %s', msg.url)
            article = get_article(msg.url)
            result = s.stats_text_cn(article)[0].most_common(20)
            image_path = path.join(cwd,'stats.png')
            plotting(result,image_path)
            msg.reply_image(image_path)
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == "__main__":
    main()

