
import requests
import matplotlib.pyplot as plt

from os import path
from pyquery import PyQuery
from mymodule import stats_word_day10
from wxpy import *

# input a weixin's article url, and then return a sorted word dict.
def sort_text(url):
    response = requests.get(url)
    document = PyQuery(response.text)
    r_content = document('#js_content').text()

    # input text and define output word numbers
    return stats_word_day10.stats_text_cn(r_content, 100)

def save_as_image(sorted_dict):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    
    words = [x for (x, y) in sorted_dict]
    count = [y for (x, y) in sorted_dict]   

    ax.barh(words, count, align = "center", color = "blue")
    ax.set_yticks(words)
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    ax.set_xlabel('count')
    ax.set_title('Top 100 words sorted by frequency')
    plt.savefig('result.png')



bot = Bot()
my_friend = bot.friends()

# auto reply SHARING message.
@bot.register(my_friend, SHARING)
def print_others(msg):
    sorted_dict = sort_text(msg.url)
    save_as_image(sorted_dict)

    print(msg.sender)
    msg.reply_image('result.png')

embed()


