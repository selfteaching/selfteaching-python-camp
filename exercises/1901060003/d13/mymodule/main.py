import stats_word
from os import path
import json
import re
import logging
import requests
import yagmail
from pyquery import PyQuery
import getpass
import wxpy
import matplotlib.pyplot as plt
import numpy as np
# from wxpy import *
#获取当前工作目录
cwd=path.abspath(path.dirname(__file__))
#设置中文字体
plt.rcParams['font.sans-serif']='SimHei'

logging.basicConfig(format='file:%(filename)s line:%(lineno)d message: %(message)s', level=logging.DEBUG)

def get_article(url):
    r=requests.get(url)
    document=PyQuery(r.text)
    return document('#js_content').text()

#生成图片
def generate_image(data,image_path):
    labels=[v[0] for v in data]
    widths=[v[1] for v in data]
    ypos=range(len(data))
    fig,ax=plt.subplots()
    ax.barh(ypos,widths)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_ylabel('关键字')
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path,bbox_inches='tight')

def main():
    bot=wxpy.Bot()
#     # 在 Web 微信中把自己加为好友
#     bot.self.add()
#     bot.self.accept()

# # 发送消息给自己
#     bot.self.send('能收到吗？')
#     embed()
    friends=bot.friends()
    @bot.register(friends, SHARING)
    def handler(msg):
        try:
            logging.info('sharing url=%s',msg.url)
            article=get_article(msg.url)
            result=stats_word.stats_text_cn(article,20)
            image_path=path.join(cwd,'stats.png')
            generate_image(result,image_path)
            msg.reply_image(image_path)
        except Exception as e:
            logging.exception(e)
    embed()

def test():
    article=get_article("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    result=stats_word.stats_text_cn(article,20)
    image_path=path.join(cwd,'stats.png')
    generate_image(result,image_path)

# bot = Bot()

# # 估计会用到Bot.chats 获取所有聊天对象
# #但实际上需要所有的聊天内容的判断，也许用 bot.search(Sharing)
# #更应该做的是search Bot.message
# # for message in Bot.message:
#       if Message.type=SHARING
#       url=Message.url, sender=Message.sender
#       Message.reply()
# @bot.register()
# def print_messages(msg):
#     print(msg)

# # 堵塞线程，并进入 Python 命令行
# embed()
# # import wxpy
# from wxpy import *
# bot = wxpy.Bot()
# # Bot.messages
# # if Message.type==SHARING:
# #     url=Message.url
# #     reply Message.sender
# my_friend=bot.friends().search('年华似水',sex='MALE',city="深圳")
# embed()

# url="https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
# r=requests.get(url)
# document=PyQuery(r.text)
# content=document('#js_content').text()
# # print(content)
# print(type(content))






# # def load_file():
# #     '''
# #     1.
# #     下面是常用的获取文件路径的方式，要确保 tang300.json 跟当前文件在同一文件夹下，这两种方式等价
# #     file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')
# #     '''
# #     file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
# #     print('当前文件路径：', __file__, '\n读取文件路径：', file_path)

# #     '''

# #     2.
# #     这种方式表示 tang300.json 在当前文件的上一级目录
# #     file_path = path.join(path.dirname(path.abspath(__file__)), '../tang300.json')
# #     print(__file__, file_path)

# #     3.
# #     这种方式表示 tang300.json 在当前文件的上一级目录的 data 文件夹下
# #     file_path = path.join(path.dirname(path.abspath(__file__)), '../data/tang300.json')
# #     print(__file__, file_path)
# #     '''

# #     with open(file_path, 'r', encoding='utf-8') as f:
# #         return f.read()


# # def merge_poems(data):
# #     poems = ''
# #     for item in data:
# #         poems += item.get('contents', '')
# #     return poems


# def main():
#     s=stats_word.stats_text(content, 100)    
#     print(type(s))
#     newtype=str(s)
#     type(newtype)
#     print(type(s))
#     print(s)
#     sender = input('输入发件人邮箱：')
#     password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
#     recipients = input('输入收件人邮箱:')
#     yag=yagmail.SMTP(sender,password,'smtp.qq.com')
#     yag.send(recipients,'自学训练营学习5群 Day11 williswill',str(s))

#     # 自学训练营学习5群 Day11 williswill
#     # 结果如下：
#     print(s)
#     # try:
#     #     data = load_file()
#     #     #logging.info(data[0])
#     #     poems = merge_poems(json.loads(data))
#     #     logging.info('result ==> %s', stats_word.stats_text_cn(poems, 100))
#     # except Exception as e:
#     #     logging.exception(e)
#delete all this in Day12


if __name__ == "__main__":
   # main()
   test()