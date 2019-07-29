from mymodule_day12 import stats_word as sw
import requests
from pyquery import PyQuery
#from wxpy import * error notification resolved by issue #1169
from wxpy import Bot,Message,embed




def main():
    bot = Bot(cache_path=True)#扫描二维码登陆微信 #issue1195 avoiding scanning again shortly
    my_friend = bot.friends()#回复对象为所有好友
    @bot.register(my_friend)
    @bot.register(msg_types='Sharing')#监听好友分享的消息 why 'Sharing'expression? SHARING got errors why oh why? input distinguish problems again?
    def auto_reply(msg):
        response = requests.get(msg.url)#msg.url为分享的网址
        document = PyQuery(response.text)
        content = document('#js_content').text()
        #像d11一样处理文本
        result = sw.stats_text_cn(content,count=10)
        wechat_word = ''.join(str(i)for i in result) # seems better str this type in case causing trouble in reading
        return wechat_word#将结果返回给好友

    embed()#d堵塞线程，保持监听

if __name__=='__main__':
    main()

#plan B copied from @wangrui0802 including day 13 codes required to be clarified
#from wxpy import *
#import d11_training1 as st
#import d13_training3 as fg
#bot = Bot()

# 找到好友并发消息
#my_friend = bot.friends()

# 获取分享文章url
#@bot.register(my_friend)
#def get_msg (msg) :
#    if msg.type == 'Sharing' :
#        retext = st.stats(msg.url, 5)
#        remsg = fg.chartImg(retext)
#        msg.reply_image(remsg)
#    else :
#        pass
#embed()
