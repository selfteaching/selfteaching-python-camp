


from mymodule.stats_word import stats_text as a
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np

# 初始化机器人，扫码登陆
bot=Bot()
#定位好友豆彭

my_friend = bot.friends().search('豆彭')  #定位朋友
#预先注册，利用Bot.register()完成
#Bot.register(chats=None,msg_types=None,except_self=True,run_async=True,enable=True)
@bot.register(chats = my_friend,msg_tyapes = 'Sharing',except_self = True)
def auto_reply(msg):
    import requests
   
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

    msg.reply_image('Word_frequency_chart.jpg')##回复图
   
embed()