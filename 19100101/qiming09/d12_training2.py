# this is d12 excercise for 3rd-party library wxpy
# date : 2019.3.29
# author by : qiming

# updat date : 2019.3.30
# content : modify reply message type.
# update by :qiming

from wxpy import Bot,Message,embed
import d11_training1 as st
import d13_training3 as fg

# 初始化机器人
bot = Bot()
my_friend = bot.friends()

# 监听分享消息,并回复分析结果
@bot.register(my_friend)
def get_msg (msg) :
    if msg.type == 'Sharing' :
        retext = st.stats(msg.url,5)
        remsg = fg.chartImg(retext)
        msg.reply_image(remsg)
    else :
        pass
embed()
