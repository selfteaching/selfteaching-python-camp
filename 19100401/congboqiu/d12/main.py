import re
import jieba
import getpass
import yagmail
import stats_word

#导入模块wxpy，建微信机器人
import sys
sys.path.append('c:\\users\\win10\\appdata\\local\\programs\\python\\python37\\lib\\site-packages')
from wxpy import *
bot=wxpy.Bot(cache_path=True)
myself=bot.self#机器人自身作为一个聊天对象

#获取聊天对象
#bot.self.add()#微信中把自己加为好友
#bot.self.accept()
#bot.file_helper.send('hello from bobohu!')#发消息给文件助手
#bot.add_friend('上山虎',verify_content='你好')#加朋友
#bot.accept_friend('上山虎',verify_content='你好')
#my_friend.send('你好，很高兴认识你。')#发消息给朋友
my_friend=bot.friends().search('翕羊羊')[0]
@bot.register()
def print_others(msg)
    print(msg)
@bot.register(my_friend,msg_types='Sharing')
def auto_reply(msg):
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    text=content
    print(text)
    str_text=str(stats_word.stats_text(text,100))
return my_friend.send('str_text')

wxpy.embed()

