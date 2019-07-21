import mymodule.stats_word as stats_word
import requests
from pyquery import PyQuery
import yagmail
import getpass

# coding:utf-8  
import json
import requests
from wxpy import *
 
 
bot = Bot(cache_path=True)#登录缓存

print('姜翔AI已经启动')

#自动词频统计机器人
def auto_ai(text):
    try:
        url = text
        response = requests.get(url,verify = False)
        document = PyQuery(response.text) 
        content = document('#js_content').text()
        #对列表中中英文字符，进行统计降序排列
        sort_list = stats_word.stats_text(content,100)

        return str(sort_list)

    except ValueError as result:
        print(result)
    except:
        print('未识别的异常！')

try:
    # 回复 my_friend 的消息 (优先匹配后注册的函数!)
    #my_friend = bot.friends().search("戴戴")[0]
    # 发送文本给好友
    #my_friend.send('在吗？回复下！')
    
    @bot.register(chats = [Friend])
    def forward_message(msg):
        print('[接收]'+str(msg))
        if (msg.type!='Text'):
        
            return '稍等，正在给分析词频！\n' + auto_ai(msg.url)
        else:
            print('[发送]'+'很不错！')
            return '很不错！'

    #持续监听好友
    embed()
except:
    print("该好友不存在！")
 




