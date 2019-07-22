from wxpy import Bot,Message,embed
import d11_training1 as st

# 初始化机器人
bot = Bot()
my_friend = bot.friends()

# 监听分享消息,并回复分析结果
@bot.register(my_friend)
def get_msg (msg) :
    if msg.type == 'Sharing' :
        retext = st.stats(msg.url,5)
        msg.reply_image(remsg)
    else :
        pass
embed()
