# Date : 19/03/29

from wxpy import *
import d11_training1 as st
import d13_training3 as fg
bot = Bot()

# 找到好友并发消息
my_friend = bot.friends()

# 获取分享文章url
@bot.register(my_friend)
def get_msg (msg) :
    if msg.type == 'Sharing' :
        retext = st.stats(msg.url, 5)
        remsg = fg.chartImg(retext)
        msg.reply_image(remsg)
    else :
        pass
embed()
