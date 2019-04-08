import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

def main():
    bot = Bot()     #扫描二维码登陆微信
    my_friend = bot.friends() #回复对象为所有好友

    @bot.register(msg_types=SHARING) #监听好友分享的消息
    def auto_reply(msg):
        response = requests.get(msg.url) # 分享网页msg.url 
		document = PyQuery(response.text)
		content = document('#js_content').text()  #d11 
        result = stats_word.stats_text_cn(content,count=100)
        return result   #将结果返回给好友

    embed() #111

if __name__=='__main__':
    main()