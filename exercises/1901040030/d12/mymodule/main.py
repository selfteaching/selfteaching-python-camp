import stats_word
import json
import requests
from pyquery import PyQuery
import yagmail
import getpass
from wxpy import *
bot=Bot() #登录微信
my_friend=bot.friends().search('老王')[0]#查找好友
@bot.register(my_friend) #接收“老王”的消息
 
def new_message(msg):
    if msg.type=='Sharing':#判断分享类型的消息
        
        ###下面是分析网络文章的代码。
        response = requests.get(msg.url)#获取文章的连接的内容
        document = PyQuery(response.text)
        content=document('#js_content').text()#获取文本
        count=100  #限制输出元素的变量
        try: 
            text_list= stats_word.stats_text(content,count) #调用统计汉字的函数
            text_list2=[] 
            for i in text_list: 
                text_list2.append(i[0]+':'+str(i[1])+';')#把text_list里面的元素处理成str存在text_list2里
            text_str=''.join(text_list2)#把列表转换成str
            print(text_str)
        except ValueError as identifier: 
            print('请输入字符串',identifier)

        #回复消息
        msg.reply('此文章高频用词')
        msg.reply(text_str)  
embed()#让程序一直运行
