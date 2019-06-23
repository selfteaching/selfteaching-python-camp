#1.将实战项目2中的结果生成为一张图片
#2.用图表图片替换文本发送给朋友
#Date:3/30/2019

#将实战项目1功能定义为函数
def word_frequency_analysis(url):
    #使用requests请求微信公众号链接，获取返回结果
    import requests

    response=requests.get(url)

    #将response.text用pyquery把微信公众号正文提取出来
    from pyquery import PyQuery as pq

    document=pq(response.text)
    content=document('#js_content').text()

    #使用stats_word中stats_text_cn分析统计前100词频结果
    from mymodule.stats_word import stats_text_cn as stc

    result=stc(content,20)
    result=str(result)
    return result

#引入wxpy模块
from wxpy import *
#引入numpy和matplotlib模块
import numpy as np
import matplotlib.pyplot as plt

bot=Bot(cache_path=True)    #初始化机器人

@bot.register(Friend,SHARING)   #接收SHARING类信息
def auto_reply_analysis_result(msg):  #注册自动回复词频
        result=word_frequency_analysis(msg.url) #分析通过监听获取的网页链接
        
        words=[item[0] for item in result]  #获取高频词
        frequncy=[item[1] for item in result]   #获取词频

        plt.rcdefaults()

        fig, ax =plt.subplots()
        y_pos=np.arange(len(words))

        ax.barh(y_pos,frequncy,align='center',color='green',ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words,fontproperties='SimHei')   #设置Y轴内容与字体
        ax.invert_yaxis()
        ax.set_xlabel('词频',fontproperties='SimHei')   #设置X轴标签内容与字体
        ax.set_title('前20词频统计',fontproperties='SimHei')    #设置标题内容与字体

        plt.show()  #调试，查看结果
        plt.savefig('C:\temp\Frequncy_for_day_13_excise.png')   #保存并中转结果
        return 'C:\temp\Frequncy_for_day_13_excise.png' #回复结果

embed() #保持监听