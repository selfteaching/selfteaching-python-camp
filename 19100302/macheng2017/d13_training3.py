# 1. 获取到网页内容
# 2. 使用以前写的词频统计
# 3. 发送email到自己的邮箱


from mymodule.stats_word import stats_text_cn
from mymodule.utils import request, send_email
import json
from wxpy import *
from mymodule.chart import chart
from os import path
path_file = path.dirname(path.realpath(__file__))

bot = Bot()
# text = request('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# res = stats_text_cn(text, 100)
# print('res', res)
# # print(list(res.keys()), '--------------------------', res.values())
# chart(list(res.keys()), list(res.values()))


@bot.register()
def print_others(msg):
    # print(msg.type, msg.text)
    if msg.type == 'Sharing':
        print('chat', msg.chat)
        print('sender', msg.sender)
        print(msg.text, msg.url)
        # 处理并返回
        text = request(msg.url)
        res = stats_text_cn(text, 100)
        print('res', res)
        print(res.keys(), '--------------------------', res.values())
        chart(list(res.keys()), list(res.values()))
        # res = json.dumps(res, ensure_ascii=False)
        img_path = path_file + '\\mymodule\\' + 're.png'
        print('img_path', img_path)
        msg.reply_image(img_path)
    #     pass
    print(msg)

# # 自动接受新的好友请求


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')


embed()
