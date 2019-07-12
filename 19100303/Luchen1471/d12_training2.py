#把d11练习里面的功能，先定义一个函数出来
import requests
from mymodule import stats_word
from pyquery import PyQuery
def dealwiththemsg(msg0):
    #if type(msg0) == 'Sharing': 
    response = requests.get(msg0.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    str_con = str(content)
    return str(stats_word.stats_text_cn(str_con))
    print(str(stats_word.stats_text_cn(str_con)))


from wxpy import *
bot = Bot(login_callback= True) #对回调并不理解

#Bot.enable_puid(path='wxpy_puid.pkl') #不用puid绑定也没问题吧
my_friend = bot.friends().search('小圆来了',sex=FEMALE)[0]
my_friend.send('你把文章转发给我（自动发送）') 
bot.file_helper.send('Hello from wxpy!')

@bot.register(my_friend,SHARING)                   #感觉没明白，为什么这里用SHARING，而不是在函数里用if判断。是不是官方文件我漏看了什么
def friend_sharing(msg):
    msg.reply(dealwiththemsg(msg))                 #给好友发送内容


embed()



