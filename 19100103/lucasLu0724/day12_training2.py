# 监听好友消息,获取消息网页链接
# 把获取到的连接使用DAY11作业去分析,
# 把结果返回给对应好友
#
from wxpy import * 
import requests
import yagmail
from pyquery import PyQuery as py
import mymodule.stats_word as sw
import getpass
bot =Bot()#扫码登录 
bot.enable_puid()

# 自动响应各种信息
@bot.register()
def print_others(msg):
    print(msg)

# 借鉴网上例子
# 打印所有*群聊*对象中的*文本*消息
# @bot.register(Group, TEXT)
# def print_group_msg(msg):
#     print(msg)

my_friend =bot.friends()

@bot.register(my_friend,SHARING)
def auto_reply_sharing_msg(msg):
    print("收到新消息:",msg)
    url=msg.raw.get('Url')
    print("对应的url:",url)
    need_reply_friend=msg.sender
    print("需要回应的朋友",need_reply_friend)

    r = requests.get(url)#获取网页数据
    web_text =r.text#使用变量web_text保护网页文本数据(这时会保存很多js代码以及其他function的代码,并不是里面所有的东西是我们需要的)
    document=py(web_text)
    content =document('#js_content').text()#js_content 是网页主文内容的div ,id为js_content,以后我们爬不同的数据,需要去看一下别人家的网页代码
    # print(content)#测试看一下得回来的数据是什么
    result =sw.stats_text_cn(content,100,False)
    result=str(result)
    need_reply_friend.send_msg(result)



embed()