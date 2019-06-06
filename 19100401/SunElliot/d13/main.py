from os import path
import json
import re
import collections
import io
import sys
from collections import Counter               
import jieba
import requests
from pyquery import PyQuery
import getpass
import yagmail
from wxpy import Bot,SHARING,embed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


bot = Bot(login_callback=True)


my_friend = bot.friends().search('Steve')

@bot.register()              #打印来自好友的消息
def print_other(msg):
    print(msg)

@bot.register(my_friend)         #回复my_friend的消息
def reply_my_friend(msg):
    return 'received:{}({})'.format(msg.text,msg.type)



# 中文字频分析

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def stats_text_cn(stri):  
    '''【注】:stats_text_cn()函数为每个汉字统计的次数如下： '''  
    if type(stri) != str:
     raise ValueError("This is not string!")
    dictionary={}                                      
    entext2=""              
    for i in stri:
     if u'\u4e00' <= i <= u'\u9fa5':                    
         entext2+=i
    #cnt=Counter()
    count=100
    #for i in entext2:  
        #cnt[i]+=1  

    seg_list=jieba.cut(entext2,cut_all=False,HMM=False)
    poem_string = "/".join(seg_list)
    poem_string = poem_string.split("/")
    for i in poem_string:
         dictionary[i] = poem_string.count(i)
    dictionary = collections.Counter(dictionary).most_common(count)
    print(stats_text_cn. __doc__) 
    print(dictionary)
    return dictionary



@bot.register(msg_types=SHARING)#监听好友分享的消息
def auto_reply_analysis_result(msg):
    response=requests.get('msg.url') 
    document = PyQuery(response.text) 
    paper_content = document('#js_content').text()
    
    result = {}

    result=stats_text_cn(paper_content)
    
    np_list=np.array(result)        #将文本处理结果转化为二维数组
    word_list=[] #初始化盛放词的列表
    number_list=[] #初始化盛放词频的列表
    for i in range(len(np_list)): #拆分Numpy多维数组
        word_list+=[np_list[i][0]]
        number_list+=[int(np_list[i][1])]
    plt.rcdefaults()
    axis=plt.subplot()
    
    y_pos = np.arange(len(word_list))
    axis.barh(y_pos, number_list, align='center', color='green', ecolor='black')
    axis.set_yticks(y_pos)
    axis.set_yticklabels(word_list)
    axis.invert_yaxis()
    axis.set_xlabel('词频')
    axis.set_title('好友分享文章词频统计')
    plt.savefig("stats.png") #保存图片
    msg.reply_image("stats.png") #回复图片
    

embed()

# 取消发送邮件功能
    #sender = input('请输入发件人邮箱：')
    #password = getpass.getpass('请输入发件人邮箱密码：')
    #recipients = 'pythoncamp@163.com'

    #yagmail.SMTP(sender,password,'smtp.163.com').send(recipients,'19100401 SunElliot',result)
