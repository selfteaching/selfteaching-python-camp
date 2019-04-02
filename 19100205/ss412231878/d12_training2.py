from wxpy import *
from pyquery import PyQuery
import requests
from mymodule import stats_word
import d13_training3

def main():#这里与最后的命名保持一致
    bot = Bot()#登录微信的命令
    my_friend = bot.friends()#发给所有好友

    #@bot.register(msg_types=SHARING)#接收分享类信息
    #def reply_my_friend(msg):#设置返回day11一样的词频统计
    #    wechat = requests.get(msg.url)
    #    document = PyQuery(wechat.text)
    #    content = document('#js_content').text()
    #    wx = stats_word.stats_text(content)
    #    wechat_word = ''.join(str(i) for i in wx)
               
    #    return wechat_word
    @bot.register(msg_types=SHARING)#接收分享类信息
    def reply_my_friend(msg):#设置返回day11一样的词频统计
        if msg.type == "Sharing":
            word = []
            number = []

            wechat = requests.get(msg.url)
            document = PyQuery(wechat.text)
            content = document('#js_content').text()
            wx = stats_word.stats_text(content)
            wechat_word = ''.join(str(i) for i in wx) 
            for i in wx:
                word.append(i[0])
                number.append(i[1]) 
            print (word)
            print(number)

            p = d13_training3.counter_stats(word,number)            
            #my_friend.send(msg)
            #my_friend.send(wx)
            my_friend.send_image('counter_stats.jpg')


    embed()#让程序执行到这里后返回，以便于重新执行

if __name__=='__main__':#这条语句能够帮助windows正常系统执行上面部分代码
    main()