import requests
import pyquery
import stats_word 
import sys
import matplotlib.pyplot as plt
import numpy as  np

#用系统的中文字体
from matplotlib.font_manager import FontManager, FontProperties
def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

from wxpy import *
bot=Bot()

my_friend=bot.friends().search('hpcs',sex=FEMALE,city='黄山')[0]

my_friend.send('我是你的朋友***。')

#打印接收到的消息
mdict=[]
mdictW=[]
mdictN=[]
strResult=''
@bot.register(my_friend)
def print_others(msg): 
    #print(msg)
    if msg.type=="Sharing":
        r=requests.get(msg.url)
        document=pyquery.PyQuery(r.text)
        content=document("#js_content").text()
        #调用stats_word中的stats_text_cn函数统计词频
        mdict=stats_word.stats_text_cn(content,10)
        for temp in mdict:
            mdictW.append(temp[0])
            mdictN.append(temp[1])
        strResult=','.join([str(x) for x in mdict])
        #用结果画图
        plt.rcdefaults()
        fig,ax=plt.subplots()
        people=mdictW
        y_pos=np.arange(len(people))
        performance=np.array(mdictN)
        ax.barh(y_pos,performance,align='center',color='green',ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people,fontproperties=getChineseFont())
        ax.invert_yaxis()
        ax.set_xlabel('词频统计结果',fontproperties=getChineseFont())
        ax.set_title('词频统计结果',fontproperties=getChineseFont())
        plt.savefig('test.jpg')
        #把文字和图片发给好友
        my_friend.send(strResult)
        my_friend.send_image('test.jpg')


# #回复my_friend的消息
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'received:{}({})'.format(msg.text,msg.type)

#自动接受心得好友请求
# @bot.register(msg_ypes=FRIENDS)
# def auto_accept_friend(msg):
#     #接受好友请求
#     new_friend=msg.card.accept()
#     #向新的好友发送消息
#     new_friend.send('哈哈！')

#进入Python命令行，让程序保持运行
embed()

# #堵塞进程
# bot.join()

# #回复my_friend
# #提取微信公众号文章正文
# r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',auth=('user','pass'))
# document=pyquery.PyQuery(r.text)
# content=document('#js_content').text()

# #调用stats_word中的stats_text_cn函数统计词频
# mdict=[]
# strResult=''
# try:
#     mdict=stats_word.stats_text_cn(content,100)
# except:
#     print("error:",sys.exc_info()[0])

# strResult=','.join([str(x) for x in mdict])