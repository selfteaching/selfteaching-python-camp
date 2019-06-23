# 1.安装numpy,matplotlib
# 2.学会使用matplotlib转换成图片然后发给对应的朋友
# 朋友发了一个sharing 的消息,转换成text 然后再转换成dict or mutlup
# 之前的功能如何转能用的格式
import matplotlib.pyplot as plt
import numpy as np
import mymodule.stats_word as sw
from wxpy import * 
import requests
import yagmail
from pyquery import PyQuery as py
import getpass

plt.rcdefaults()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
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

# @bot.register(my_friend,SHARING)
# def auto_reply_sharing_msg(msg):
#     print("收到新消息:",msg)
#     url=msg.raw.get('Url')
#     print("对应的url:",url)
#     need_reply_friend=msg.sender
#     print("需要回应的朋友",need_reply_friend)

#     r = requests.get(url)#获取网页数据
#     web_text =r.text#使用变量web_text保护网页文本数据(这时会保存很多js代码以及其他function的代码,并不是里面所有的东西是我们需要的)
#     document=py(web_text)
#     content =document('#js_content').text()#js_content 是网页主文内容的div ,id为js_content,以后我们爬不同的数据,需要去看一下别人家的网页代码
#     # print(content)#测试看一下得回来的数据是什么
#     result =sw.use_jieba_calculate(content)
#     result=str(result)
#     need_reply_friend.send_msg(result)

@bot.register(my_friend,SHARING)
def auto_reply_sharing_photo(msg):
    print("接受到新消息:",msg)
    url=msg.raw.get("Url")
    print("对应的url:",url)
    need_reply_friend=msg.sender
    print("需要回应的朋友",need_reply_friend)
    r = requests.get(url)#获取网页数据
    web_text =r.text#使用变量web_text保护网页文本数据(这时会保存很多js代码以及其他function的代码,并不是里面所有的东西是我们需要的)
    document=py(web_text)
    content =document('#js_content').text()#js_content 是网页主文内容的div ,id为js_content,以后我们爬不同的数据,需要去看一下别人家的网页代码
    print("content",content)
    result_list =sw.use_jieba_calculate(content)
    print("reusult_list",result_list)
    need_reply_friend.send_msg(str(result_list))
    #返回结果处理部分
    x_ax=[]
    y_ax=[]
    for item in result_list:
        x_ax.append(item[0])
        y_ax.append(item[1])
    #图表部分
  
    fig, ax = plt.subplots()
    # Example data
    y_pos = np.arange(len(x_ax))
    performance = y_ax
    error = np.random.rand(len(x_ax))
    ax.barh(y_pos, performance, xerr=error, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(x_ax)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('字符')
    ax.set_title('How fast do you want to go today?')
    plt.savefig("examples.jpg")
    need_reply_friend.send_image('examples.jpg')
    plt.show()





embed()