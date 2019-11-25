
import logging
import requests
import pyquery
from wxpy import *
from mymodule import stats_word
import matplotlib 
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

#提取微信公众号文章正文
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def handler(msg):
        try:
            logging.info('sharing url = %s',msg.url)
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article,100)
           #####################对词频统计结果进行图形化处理
            ll_words = []
            ll_nums  = []
            for ll in requests:
                ll_words.append(ll[0])
                ll_nums.append(ll[1])
            np.random.seed(19680001)
            plt.rcdefaults()
            fig,ax = plt.subplot()
            y_pos = np.arange(len(ll_words))
            error = np.random.rand(len(ll_words))

            ax.barh(y_pos,ll_nums,xerr = error,align = 'center')
            ax.set_yticks(y_pos)
            ax.set_yticklabels('ll_words')
            ax.invert_yaxis()
            ax.set_xlabel('ll_nums')
            ax.set_title('词频输出排序')
            

            msg.reply(str(fig))
        except Exception as e:
            logging.exception(e)
    embed()

    


if __name__ == '__main__':
    main()

