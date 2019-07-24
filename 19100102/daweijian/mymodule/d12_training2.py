from wxpy import Bot, embed
from d11_training import request_data

#扫描二维码登陆微信
bot = Bot()
my_friend=bot.friends().search('梓森',sex=FEMALE,city='揭阳')[0]

my_friend.send('程序测试：转发任意微信推文给我，完成测试')

# 消息接收监听器
@bot.register()
def print_others(msg):
    # 输出监听到的消息
    print(msg)
    if msg.type == 'Sharing':
        s = request_data(msg.url)
        print(s)
        msg.reply(s)


embed()
