from mymodule import stats_word
from os import path
import logging
import requests
import pyquery
import matplotlib.pyplot as plt
from wxpy import *

# 安装依赖包 wxpy
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple wxpy

# 获取当前工作路径
cwd = path.abspath(path.dirname(__file__))
# 设置中文字体
plt.rcParams['font.sans-serif'] = 'SimHei'

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)


# 提取微信公众号文章正文
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


# 生成图片
def generate_image(data,image_path):
    labels = [v[0] for v in data]
    widths = [v[1] for v in data]
    ypos = range(len(data))
    fig, ax = plt.subplots()
    ax.barh(ypos, widths)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_ylabel('关键字')
    ax.set_title('词频')
    fig.savefig(image_path, bbox_inches='tight')



def main():
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def handler(msg):
        try:
            logging.info('sharing usr = %s',msg.url)
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article,100)
            image_path = path.join(cwd, 'stats.png')
            generate_image(result,image_path)
            msg.reply(str(result))
        except Exception as e:
              logging.exception(e)
    embed()


def test():
    article = get_article('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    result = stats_word.stats_text_cn(article, 20)
    image_path = path.join(cwd, 'stats.png')
    generate_image(result, image_path)


if __name__ == "__main__":
    main()
    # test()


