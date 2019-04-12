from mymodule import stats_word
import requests
import pyquery
import wxpy 

bot = wxpy.Bot()
my_friend = bot.friends().search()
@bot.register()
def print_others(msg):
    print(msg)

@bot.register(my_friend,msg_types='Sharing') #接受分享类消息
def auto_reply(msg):
        response = requests.get(msg.url) #msg.url为分享的网址
        document = pyquery.PyQuery(response.text)
        content = document('#js_content').text()
        #处理文本
        result = content
        print(result)
wxpy.embed()