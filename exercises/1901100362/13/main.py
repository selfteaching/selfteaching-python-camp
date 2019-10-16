from matplotlib import rcParams
from mymodule import stats_word
import traceback
import logging
import json
from os import path
import yagmail
from pyquery import PyQuery
import requests
import matplotlib.pyplot as plt
from wxpy import *
import numpy as np
from pylab import mpl


def test_traceback():
    try:
        stats_word.stats_text(text)
    except Exception as e:
        print("trace_back==>", e)
        print(traceback.format_exc())


def test_logger():
    try:
        stats_word.stats_text(text)
    except Exception as e:
        logging.exception(e)


def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
    print("当前文件路径==>", __file__, '\n读取文件路径==>', file_path)
    '''
  tang300.json在上一级目录
  file_path = path.join(path.dirname(path.abspath(__file__)),'../tang300.json')

  tang300.json文件在上一级目录的data目录下的文件
  file_path = path.join(path.dirname(path.abspath(__file__)),'../data/tang300.json')
  '''

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


# data为由json转换而来的字典
def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems


def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(r.text)
    return document('#js_content').text()


def main():
    try:
        '''
    bot = Bot()
    my_friend = bot.my_friends()

    @bot.register(my_friend,SHARING)
    def auto_reply(msg):
      response = requests.get(msg.url)
      document = PyQuery(response.text)
      content = document('#js_content').text()
    '''
        article = get_article()
        result = stats_word.stats_text_cn(article, 10)

        np_list = np.array(result)
        word_list = []
        number_list = []

        for i in range(len(np_list)):
            word_list += [np_list[i][0]]
            number_list += [int(np_list[i][1])]

        plt.rcdefaults()

        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        # plt.rcParams['axes.unicode_minus'] = False
        fig,ax = plt.subplots()
        y_pos = np.arange(len(word_list))

        ax.barh(y_pos, number_list, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(word_list)
        ax.invert_yaxis()
        ax.set_xlabel('计数')
        ax.set_title('词频统计')
        # plt.savefig("stats.png")
        plt.show()

        embed()

    except Exception as e:
        logging.exception(e)
if __name__ == '__main__':
    main()
