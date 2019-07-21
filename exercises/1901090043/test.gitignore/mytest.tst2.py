# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

# 搜索名称含有 "游否" 的男性深圳好友
my_friend = bot.friends().search('么么哒')[0]

# 发送文本给好友
my_friend.send('Hello WeChat!合作吗？')
# 发送图片
#my_friend.send_image('贝莉儿-ng-bviex5lwf3s.jpg')

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    #return '回复: {} ({})'.format("你的好友不在线！", msg.type)
    return '回复：{}'.format('你的好友现在在忙！')


# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
    

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')


embed()
