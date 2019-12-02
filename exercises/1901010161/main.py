# 导入模块
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from wxpy import *
import yagmail
import requests
from pyquery import PyQuery
import getpass
import logging
from mymodule import stats_word

# 安装依赖包 requests yagmail pyquery lxml
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests yagmail pyquery lxml

logging.basicConfig(format='file:%(filename)s|line:%(lineno)s|message:%(message)s',level=logging.DEBUG)

# 通过 requests.get 获得 URL网页的文章，存入 response  并返回
def get_article(url):
    response = requests.get(url)
    document = PyQuery(response.text)
    return document('#js_content').text()

def main():

        # 初始化机器人，扫码登陆
        bot = Bot()
        
        # 搜索好友
        my_friends = bot.friends().search('金融家')[0]

        # 监听 my_friend 的分享的消息，并获得分享消息的 链接
        @bot.register(chats=my_friends)
        def proc(msg):
            try:
                logging.info('sharing url - %s', msg.url)
                article = get_article(msg.url)
                count = 10
                result = stats_word.stats_text_cn(article, count)  # 调 stats_text_cn ，将所汉字及频次记录 result
                
                group_data = list(result.values())
                group_names = list(result.keys())

                y_pos = np.arange(len(group_names))
                
                plt.rcdefaults()
                fig, ax = plt.subplots()
                plt.rcParams['font.sans-serif']=['SimHei'] 
                ax.barh(y_pos, group_data, align='center')
                ax.set_yticks(y_pos)
                ax.set_yticklabels(group_names)
                ax.invert_yaxis()
                ax.set_xlabel('词频')
                ax.set_title('网页中TOP10中文词语') 
                plt.savefig(r'wordsCnt.jpeg')
                msg.reply_image(r'wordsCnt.jpeg')

            except Exception as e:
                logging.exception(e)

        # 进入 Python 命令行、让程序保持运行         
        embed() 

if __name__ == '__main__':
    main()