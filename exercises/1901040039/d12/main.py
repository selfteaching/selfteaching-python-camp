import mymodule.stats_word
import requests
from pyquery import PyQuery
from wxpy import *  #import * 把一个模块的所有内容全都导入到当前的命名空间

def main():
    bot = Bot() #  扫描二维码登陆微信
    my_friend = bot.friends()#  初始化机器人，扫描登录
    

    @bot.register(my_friend,SHARING)#接受分享类消息（SHARING)
    def auto_reply(msg):
        response = requests.get(msg.url)#msg.url为分享的地址(解析文章的url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        #处理文本
        result = mymodule.stats_word.stats_text_cn(content,count=100)
        return result  #把结果返回给朋友

    embed()  #进入 Python 命令行、让程序保持运行，(保持监听状态)

if __name__=='__main__':
     main()


# path = r'D:\用户目录\selfteaching-python-camp\exercises\1901040039\d10\tang300.json'
# with open(path,'r', encoding='UTF-8') as f:
#     #不加'r', encoding='UTF-8'会报UnicodeDecodeError
#     read_date = f.read()
# f.closed

# try:
#     print('前20的词频数：\n',mymodule.stats_word.stats_text_cn(read_date,20))
# except ValueError as w:
#     print(w)
#     print(os.path.dirname(os.path.realpath(__file__)))

#     导入模块
# from wxpy import *
# 初始化机器人，扫码登陆
# bot = Bot()


# 找到好友:
# 搜索名称含有 "游否" 的男性深圳好友
# my_friend = bot.friends().search('游否', sex=MALE, city="深圳")[0]

# 发送消息:
# 发送文本给好友
# my_friend.send('Hello WeChat!')
# 发送图片
# my_friend.send_image('my_picture.jpg')

# 自动响应各类消息:
# 打印来自其他好友、群聊和公众号的消息
# @bot.register()
# def print_others(msg):
#     print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求
# @bot.register(msg_types=FRIENDS)
# def auto_accept_friends(msg):
#     接受好友请求
#     new_friend = msg.card.accept()
#     向新的好友发送消息
#     new_friend.send('哈哈，我自动接受了你的好友请求')
# 保持登陆/运行:
# 进入 Python 命令行、让程序保持运行
# embed()

# 或者仅仅堵塞线程
# bot.join()