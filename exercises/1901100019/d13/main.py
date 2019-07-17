from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import numpy as np

def get_url_data(url):
    r = requests.get(url)
    document = PyQuery(r.text)
    content = document('#js_content').text()
    return content

def draw_graph(array_x, array_y, image_name):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
    zhfont1 = font_manager.FontProperties(fname="SimHei.ttf")

    ax.bar(array_x, array_y, align='center')
    ax.set_xticklabels(array_x, fontproperties=zhfont1)

    ax.set_xlabel('word', fontproperties=zhfont1)
    ax.set_ylabel('num', fontproperties=zhfont1)
    ax.set_title('词频统计', fontproperties=zhfont1)
#    plt.show()
    plt.savefig(image_name)

def main():
    save_image_name = 'graph.png'

    bot = Bot(cache_path=True)
    my_friend = bot.friends().search('icansee')[0]

    @bot.register([my_friend])
    def print_messages(msg):
        print(msg)

        if msg.type == 'Sharing':
            text = get_url_data(msg.url)
            
            result = stats_word.stats_text_cn(text, 10)
            print(result)
            msg.reply('文章中最常出现的前10个词：' + str(result))

            array_x = []
            array_y = []
            for i in range(len(result)):
                array_x.append(result[i][0])
                array_y.append(result[i][1])

            draw_graph(array_x, array_y, save_image_name)
            msg.reply_image(save_image_name)

    embed()

if __name__ == '__main__':
    main()