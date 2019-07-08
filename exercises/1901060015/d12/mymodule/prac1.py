from wxpy import *
import requests
from pyquery import PyQuery
import stats_word

bot = Bot(cache_path= True)

#机器人账号自身
myself =bot.self

my_friend =bot.friends()
msg = bot.messages

@bot.register(my_friend,SHARING)
def get_msgurl(msg):
    return Message.url

url=get_msgurl(msg)

r = requests.get("url")
#提取正文
d=PyQuery(r.text)
c=d('#js_content').text().replace("，","").replace("。","").replace("\n","")

c1 = stats_word.stats_text_cn(c)
#转换为字符串
c2 =str(c1)






    
    















