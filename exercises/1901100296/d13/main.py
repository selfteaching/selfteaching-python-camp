from mymodule import stats_word
import getpass
import yagmail
from wxpy import *
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
from os import path

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message:%(message)s',level=logging.DEBUG)

file_path = path.join(path.dirname(path.abspath(__file__)),'SimHei.ttf')

# 将统计结果画成条形图并返回条形图的保存路径
def stats_barplot(list_data):
    zhfont1 = matplotlib.font_manager.FontProperties(fname=file_path)

    words = [x[0] for x in list_data ]
    frequence = [x[1] for x in list_data]

    fig,ax = plt.subplots()
    ax.barh(words,frequence)
    ylabels = ax.get_yticklabels()
    plt.setp(ylabels,FontProperties=zhfont1)
    ax.set_xlabel('词频',FontProperties=zhfont1)
    ax.set_ylabel('词语',FontProperties=zhfont1)
    ax.set_title('文章中出现次数在前10的词语',FontProperties=zhfont1)
    png_path = path.join(path.dirname(path.abspath(__file__)),'stats_words_barplot.png')
    fig.savefig(png_path,transparen=False,dpi=80,bbox_inches="tight")
    # plt.show()
    return png_path

def main():
    # 初始化机器人，扫码登录
    bot = Bot()
    # 找到好友和群聊
    my_friends = bot.friends()
    # family_group = bot.groups()

    # 监听好友信息，自动响应分享类型的消息
    @bot.register(my_friends,SHARING)
    def handler(msg):
        try:
            logging.info('sharing url=%s',msg.url)
            msg.reply(stats_barplot(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == '__main__':
    main()

