# encoding=utf-8
from wxpy import *
import jieba
import yagmail
import requests
from pyquery import PyQuery
from collections import Counter

from mymodule import stats_word
import getpass
import logging

import matplotlib.pyplot as plt
import matplotlib.image as imagedeal
import numpy as np
from pylab import *


from matplotlib.font_manager import FontProperties
# 提取字体对象
font = FontProperties(fname='/Library/Fonts/Songti.ttc')

# 提取公众号文章里的正文内容并统计词频前100的词汇

def get_article_hotwords(path,count):
    # 链接获取的内容
    response = requests.get(path, auth=('user', 'pass'))
    # 提取正文
    document = PyQuery(response.text) 
    # 返回正文字符串
    content = document('#js_content').text()
    word_list =  stats_word.stats_text_cn(content,count)
    words = []
    for item in word_list:
        words.append(item[0])
    words = ','.join(words)
    return words


# sender:发送者，不能为空
# author_key：发送者邮箱的授权码
# host：邮箱服务器类别
# subject：邮件标题
# message：邮件正文
# recepients = None：接受者

def send_mail(sender,author_key ,host, subject,message,recipients = None):
    try: 
        # print(sender,author_key ,host, subject,message,recipients)
        mail = yagmail.SMTP(sender, author_key,host)
        mail.send(recipients, subject,message)
        print("发送结束")
    except EnvironmentError:
        print("登录失败")
    except ValueError:
        print("参数类型或者数量有错")

sender = "danagcong@163.com"
    # password = getpass.getpass('dangcong1993') 
author_key = "dangcong1993"
host = 'smtp.163.com'
subject = "自学营009期01班 day12 党聪 "
# '自学营009期01班 JiJun-1993'
recipients = ["pythoncamp@163.com",sender]

image_path = "/Users/mac/Desktop/selfteaching-python-camp/exercises/1901050107/d13/image/temp.png"
def graph_data(item_list):
# Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(item_list))
    performance = 3 + 10 * np.random.rand(len(item_list))
    error = np.random.rand(len(item_list))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(item_list,fontproperties = font)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('出现次数',fontproperties = font)
    ax.set_title("你发我的文章中的关键词统计",fontproperties = font)
    plt.savefig(image_path)
    return image_path



# 初始化机器人，扫码登陆
bot = Bot()

@bot.register([Friend])#当好友发消息给你时，执行下面的函数
def print_others(msg):
    if msg.type == "Sharing":
    # 获取文章中关键词组成的字符串
        context = get_article_hotwords(msg.url,20)
        # 把字符串对性转化为元组
        context = tuple(context.split(','))
        result = graph_data(context)
        msg.reply_image(result)
        # send_mail(sender,author_key ,host, subject,context,recipients)
        print("回复成功")
    else:
        print(msg)
embed()    

