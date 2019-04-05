# 1. 获取到网页内容
# 2. 使用以前写的词频统计
# 3. 发送email到自己的邮箱


from mymodule.stats_word import stats_text_cn
from mymodule.utils import request, send_email
import json
from wxpy import *
bot = Bot()
# print(r.status_code)

# print(r.headers['content-type'])

# print(r.encoding)
# text = request('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
# res = stats_text_cn(text,0)
# res =json.dumps(res,ensure_ascii=False)
# # send_email(res)
# print(res)
# # print(r.text)


# 1. 登录微信,监听好友信息,获取好友的发的链接
# 2. 使用词频统计函数
# 3. 将结果发给发链接的好友

# 搜索名称含有 "游否" 的男性深圳好友
# my_friend = bot.friends().search('游否', sex=MALE, city="深圳")[0]
# # 发送文本给好友
# my_friend.send('Hello WeChat!')
# # 发送图片
# my_friend.send_image('my_picture.jpg')

# 打印来自其他好友、群聊和公众号的消息


@bot.register()
def print_others(msg):
    # print(msg.type, msg.text)
    if msg.type == 'Sharing':
        print('chat',msg.chat)
        print('sender',msg.sender)
        print(msg.text, msg.url)
        # 处理并返回
        text = request(msg.url)
        res = stats_text_cn(text,100)
        res =json.dumps(res,ensure_ascii=False)
        msg.reply(res)


    #     pass
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)


# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')


embed()
