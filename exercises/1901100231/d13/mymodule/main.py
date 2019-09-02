import json#加载json模块完成对.json文件的读取
import stats_word
import requests
from pyquery import PyQuery
from wxpy import *#加载wxpy模块中所有函数
from matplotlib import pyplot as plt
plt.rcParams['font.family']=['SimHei']#使用系统自带的中文字体
def get_it(msg) :#定义获取网页内容的函数
    response = requests.get(msg)
    document = PyQuery(response.text)
    return document('#js_content').text()
bot = Bot()#登录账号
friend = bot.friends()#获取所有好友
@bot.register(friend,SHARING)#检测所有好友发来消息中的sharing类型的消息
def statistics(msg):#以捕获的网页连接为参数，获取其中内容的词频统计结果
    content = get_it(msg.url)#获取网页内容
    output = stats_word.stats_text_cn(content,15)#对网页内容进行词频统计（因为100个词语的词频统计过于拥挤，测试后改为只统计前15个）
    output = dict(output)#将统计得到的列表转换回字典以便取其中所有键和所有值分别作为图表的x轴和y轴
    x = list(output.keys())#横轴为统计的每个单词
    y = list(output.values())#纵轴为每个单词出现的频率
    plt.bar(x,y)#生成条形统计图
    plt.xlabel('最常用15词')
    plt.ylabel('出现次数')
    plt.title('文章最常用前15词语词频统计表')#为图表添加注释
    for a,b in zip(x,y):#为每个词语条形柱标明具体数字
        plt.text(a,b,'%.0f' % b ,ha='center',va='bottom')
    plt.savefig('chart.png')#保存文件
    msg.reply_image('chart.png')#发送文件
embed()