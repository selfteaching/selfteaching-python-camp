# 导入模块
from wxpy import *
import requests
from mymodule import stats_word_d13
from pyquery import PyQuery
'''
当好友向你发送消息后，如果为 分享 (SHARING) 类型的消息，则获取消息的网页链接（msg.url）
将获取的链接使用代码进行处理
将处理结果返回给发送消息过来的好友
'''

# 初始化机器人，扫码登陆
bot = Bot()

@bot.register(msg_types = SHARING)  
def reply_my_friend(msg):  

    #使用request请求信息中的url
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()

    #使用stats_word 中的 stats_text 对提取结果进行分析和词频统计处理（返回前20个词的统计结果），将结果转换成 str 类型
    result = str(stats_word_d13.stats_text_cn(content,20))
    
    #处理文本
    file = eval(result)
    # 将所有的单词取出组成一个元组
    words = []
    # 将所有的词频取出组成一个列表
    counts = []
    for item in file:    
        words.append(item[0])
        counts.append(item[1])
    words = tuple(words)

    #为了能在matplotlib中显示中文，需要中文字体的支持
    import matplotlib.pyplot as plt
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    # 将文章的分析结果存入numpy 中
    import numpy as np
    fig, ax =plt.subplots()
    y_pos = np.arange(len(words))
    counts = np.array(counts)
    error = np.random.rand(len(words))
  
    #绘制处理的文本为图形
    ax.barh(y_pos, counts, xerr=error, align='center',color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    ax.set_xlabel('counts')
    ax.set_title('Analysis of Chinese word frequency')
    plt.savefig('Word_frequency_chart.jpg')#保存图片

    msg.reply_image('Word_frequency_chart.jpg')##回复图片


embed()