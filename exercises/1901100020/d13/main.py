# 安装微信依赖包
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib 
from os import path
import logging
import requests
import matplotlib.pyplot as plt
import pyquery
from wxpy import *
from mymodule import stats_word

# 获取当前工作目录
cwd = path.abspath(path.dirname(__file__))
# 设置中文字体
plt.rcParams['font.sans-serif'] ='SimHei'

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)
# 提取微信公众号文章正文
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()

# 生成图片
def generate_image(data, image_path):
    labels = [v[0] for v in data]
    widths = [v[1] for v in data]
    ypos = range(len(data))
    fig, ax = plt.subplots()
    ax.barh(ypos, widths)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_ylabel('关键字')
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path, bbox_inches='tight')
    
def main():
    bot = Bot()
    friends = bot.friends()
    @bot.register(friends, SHARING)
    def handler(msg):
        try:
            logging.info('sharing url = %s', msg.url)
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article, 100)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == "__main__":
    # main()
    test()
