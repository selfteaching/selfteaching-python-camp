#導入模塊
from wxpy import *
import requests #網路請求庫
from mymodule import stats_word
from pyquery import PyQuery #文檔解析庫

#初始化機器人
bot = Bot()


@bot.register(msg_types = SHARING)

def reply_my_friend(msg):
    #使用request請求信息中的url
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
	#使用stats_word 中的  stats_text對提取結果進行分析和詞頻分析統計將結果轉成str類型
    result = str(stats_word.stats_text_cn(content,20))
    msg.reply(result) #將結果返回給發送消息的好友
	
embed()
